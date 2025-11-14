#!/usr/bin/env python3
"""
MBIE Command Line Interface

Main entry point for the Memory-Bank Intelligence Engine.
"""

# Standard library imports
import logging
import sys
import time
from pathlib import Path
from typing import Optional

# Add current directory to path for import resolution
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

# Third-party imports
import click
import yaml
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax

# Local imports - using relative imports with path resolution
from core import MemoryBankChunker, LocalEmbedder, HybridSearcher
from core.indexer import IncrementalIndexer

# Phase 2 imports (optional, handle gracefully if not available)
try:
    from core.analytics import create_analytics_system
    from core.learning import create_learning_engine
    from integrations.calendar_integration import create_calendar_integration

    PHASE2_AVAILABLE = True
except ImportError:
    PHASE2_AVAILABLE = False


# Initialize rich console for pretty output
console = Console()


def load_config(config_path: Optional[str] = None) -> dict:
    """Load configuration from YAML file"""
    if config_path:
        config_file = Path(config_path)
    else:
        # Default config location
        config_file = Path(__file__).parent / "config.yml"

    if not config_file.exists():
        console.print(f"[red]Config file not found: {config_file}[/red]")
        sys.exit(1)

    with open(config_file, "r") as f:
        return yaml.safe_load(f)


def setup_logging(config: dict):
    """Setup logging configuration"""
    # Use default logging config if not provided (for testing)
    logging_config = config.get("logging", {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file": "memory_rag.log"
    })

    logging.basicConfig(
        level=logging_config["level"],
        format=logging_config["format"],
        handlers=[
            logging.FileHandler(logging_config["file"]),
            logging.StreamHandler(),
        ],
    )


@click.group()
@click.option("--config", "-c", help="Path to config file")
@click.pass_context
def cli(ctx, config):
    """Memory-Bank Intelligence Engine (MBIE) - Intelligent documentation retrieval"""
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config)
    setup_logging(ctx.obj["config"])


@cli.command()
@click.option("--full", is_flag=True, help="Force full reindex")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.option("--quiet", "-q", is_flag=True, help="Suppress output (for automation)")
@click.option("--incremental", is_flag=True, help="Force incremental indexing")
@click.pass_context
def index(ctx, full, verbose, quiet, incremental):
    """Index or update the memory-bank documents"""
    config = ctx.obj["config"]

    # Ensure required config sections exist with defaults
    config.setdefault("intelligence", {"enabled": False})
    config.setdefault("domains", {})

    # Check automation config for silent mode
    automation_config = config.get("automation", {})
    is_silent = quiet or bool(automation_config.get("silent_mode", False))

    if not is_silent:
        console.print(
            Panel.fit(
                "[bold cyan]MBIE Indexing[/bold cyan]\n"
                "Building searchable index from memory-bank..."
            )
        )

    # Initialize components
    chunker = MemoryBankChunker(config)
    embedder = LocalEmbedder(config)
    searcher = HybridSearcher(config, embedder)
    indexer = IncrementalIndexer(config, chunker, embedder, searcher)

    # Create or load collection
    searcher.create_or_load_collection()

    # Determine what to index
    if full:
        if not is_silent:
            console.print("[yellow]Performing full reindex...[/yellow]")
        indexed_count = indexer.full_index()
    else:
        if not is_silent:
            console.print("[yellow]Checking for changes...[/yellow]")
        indexed_count = indexer.incremental_index()

    # Show statistics only if not in quiet mode
    if not is_silent:
        stats = searcher.get_statistics()

        table = Table(title="Index Statistics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Documents Indexed", str(indexed_count))
        table.add_row("Total Chunks", str(stats["total_chunks"]))
        table.add_row("Unique Documents", str(stats["unique_documents"]))
        table.add_row("🔴 Large Files", str(stats["category_distribution"]["🔴"]))
        table.add_row("🟡 Medium Files", str(stats["category_distribution"]["🟡"]))
        table.add_row("🟢 Small Files", str(stats["category_distribution"]["🟢"]))

        console.print(table)
        console.print("[green]✓ Indexing complete![/green]")

    return indexed_count


@cli.command()
@click.argument("query")
@click.option(
    "--domain",
    "-d",
    type=click.Choice(["business", "automation", "health", "philosophy"]),
    help="Filter by domain",
)
@click.option("--top-k", "-k", default=5, help="Number of results to return")
@click.option("--cite", is_flag=True, help="Show citations only")
@click.option("--verbose", "-v", is_flag=True, help="Show detailed results")
@click.option(
    "--status",
    type=click.Choice(["completed", "in_progress", "pending", "planning"]),
    help="Filter by status type",
)
@click.option("--current-only", is_flag=True, help="Show only current/active content")
@click.option("--urgent-only", is_flag=True, help="Show only urgent content")
@click.pass_context
def query(ctx, query, domain, top_k, cite, verbose, status, current_only, urgent_only):
    """Query the memory-bank index"""
    config = ctx.obj["config"]
    config["search"]["top_k"] = top_k

    # Initialize analytics system if available and enabled
    analytics_collector = None
    query_start_time = time.time()

    # Debug: Check analytics conditions
    analytics_enabled = config.get("analytics", {}).get("enabled", False)

    if PHASE2_AVAILABLE and analytics_enabled:
        try:
            analytics_collector, analyzer = create_analytics_system(config)

            # Start analytics session
            session_id = analytics_collector.start_session("mbie_cli")

            # Extract business context from intelligence config
            intelligence_config = config.get("intelligence", {})
            temporal_context = intelligence_config.get("temporal_context", {})
            business_context = f"{temporal_context.get('current_quarter', 'Unknown')} - {temporal_context.get('current_phase', 'Unknown')}"

        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.error(f"Analytics system initialization failed: {e}")
            import traceback

            logger.error(traceback.format_exc())
            analytics_collector = None

    # Initialize components
    embedder = LocalEmbedder(config)
    searcher = HybridSearcher(config, embedder)

    # Load collection
    searcher.create_or_load_collection()

    # Build intelligence filters
    intelligence_filters = {}
    if status:
        intelligence_filters["status_type"] = status
    if current_only:
        intelligence_filters["min_current_relevance"] = 0.7
    if urgent_only:
        intelligence_filters["min_urgency_score"] = 0.3

    # Perform search
    console.print(f"[cyan]Searching for:[/cyan] {query}")
    if domain:
        console.print(f"[cyan]Domain filter:[/cyan] {domain}")
    if intelligence_filters:
        console.print(f"[cyan]Intelligence filters:[/cyan] {intelligence_filters}")

    results = searcher.search(
        query, domain=domain, intelligence_filters=intelligence_filters or None
    )

    # Record analytics if enabled
    if analytics_collector:
        try:
            query_end_time = time.time()
            response_time_ms = (query_end_time - query_start_time) * 1000

            # Extract result IDs for analytics
            result_ids = [
                result.chunk.chunk_id
                if hasattr(result.chunk, "chunk_id")
                else f"chunk_{i}"
                for i, result in enumerate(results)
            ]

            # Record the query
            query_id = analytics_collector.record_query(
                query_text=query,
                search_results=result_ids,
                response_time_ms=response_time_ms,
                business_context=business_context,
            )

            # Record basic interaction (view results)
            if results:
                analytics_collector.record_interaction(
                    query_id=query_id,
                    interaction_type="view",
                    clicked_results=[],  # CLI doesn't track clicks, but records view
                    time_spent=0,  # CLI doesn't track time spent
                    satisfaction_score=None,  # CLI doesn't track satisfaction
                )

        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.warning(f"Failed to record analytics: {e}")

    # End analytics session
    if analytics_collector:
        try:
            analytics_collector.end_session()
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.warning(f"Failed to end analytics session: {e}")

    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return

    # Display results
    console.print(f"\n[green]Found {len(results)} relevant sections:[/green]\n")

    for i, result in enumerate(results, 1):
        if cite:
            # Citation mode - just show references
            console.print(f"{i}. {result.citation} (score: {result.score:.3f})")
        else:
            # Full results
            panel_content = []

            # Add navigation path
            panel_content.append(f"[dim]{result.chunk.navigation_path}[/dim]")

            # Add content preview
            content_preview = (
                result.chunk.content[:300] + "..."
                if len(result.chunk.content) > 300
                else result.chunk.content
            )
            panel_content.append(f"\n{content_preview}")

            # Add metadata if verbose
            if verbose:
                panel_content.append(
                    f"\n[dim]Type: {result.relevance_type} | Category: {result.chunk.metadata.get('size_category', '?')}[/dim]"
                )

            panel = Panel(
                "\n".join(panel_content),
                title=f"[bold]{i}. {result.citation}[/bold] [green](score: {result.score:.3f})[/green]",
                border_style="blue",
            )
            console.print(panel)


@cli.command()
@click.pass_context
def stats(ctx):
    """Show index statistics"""
    config = ctx.obj["config"]

    # Initialize components
    embedder = LocalEmbedder(config)
    searcher = HybridSearcher(config, embedder)

    # Load collection
    searcher.create_or_load_collection()

    # Get statistics
    stats = searcher.get_statistics()

    # Display statistics
    table = Table(title="MBIE Index Statistics")
    table.add_column("Metric", style="cyan", width=30)
    table.add_column("Value", style="green", width=20)

    table.add_row("Total Chunks", str(stats["total_chunks"]))
    table.add_row("Unique Documents", str(stats["unique_documents"]))
    table.add_row("Embedding Dimension", str(stats["embedding_dimension"]))
    table.add_row("", "")  # Spacer
    table.add_row("[bold]Category Distribution[/bold]", "")
    table.add_row(
        "  🔴 Large Files (>600 lines)", str(stats["category_distribution"]["🔴"])
    )
    table.add_row(
        "  🟡 Medium Files (400-600)", str(stats["category_distribution"]["🟡"])
    )
    table.add_row("  🟢 Small Files (<400)", str(stats["category_distribution"]["🟢"]))

    console.print(table)

    # Show config info
    console.print(f"\n[cyan]Configuration:[/cyan]")
    console.print(f"  Model: {config['model']['name']}")
    console.print(f"  Chunk size: {config['chunking']['chunk_size']}")
    console.print(f"  Memory bank: {config['storage']['memory_bank_root']}")


@cli.command()
@click.option("--output", "-o", help="Output file for backup")
@click.pass_context
def backup(ctx, output):
    """Backup the index and embeddings"""
    config = ctx.obj["config"]

    from .utils.backup import BackupManager

    backup_manager = BackupManager(config)

    if output:
        backup_path = Path(output)
    else:
        backup_path = None

    console.print("[cyan]Creating backup...[/cyan]")

    backup_file = backup_manager.create_backup(backup_path)

    console.print(f"[green]✓ Backup created: {backup_file}[/green]")


@cli.command()
@click.argument("backup_file")
@click.pass_context
def restore(ctx, backup_file):
    """Restore index from backup"""
    config = ctx.obj["config"]

    from .utils.backup import BackupManager

    backup_manager = BackupManager(config)

    console.print(f"[cyan]Restoring from: {backup_file}[/cyan]")

    success = backup_manager.restore_backup(backup_file)

    if success:
        console.print("[green]✓ Restore complete![/green]")
    else:
        console.print("[red]✗ Restore failed![/red]")


@cli.command()
@click.option("--full", is_flag=True, help="Run full evaluation with all test queries")
@click.option(
    "--quick", is_flag=True, help="Run quick evaluation with core metrics only"
)
@click.pass_context
def evaluate(ctx, full, quick):
    """Run evaluation on test queries with quality gates (Issue #203)"""
    config = ctx.obj["config"]

    from .evaluation import Evaluator

    console.print(
        Panel.fit(
            "[bold cyan]MBIE Evaluation[/bold cyan]\n"
            "Running evaluation on test queries..."
        )
    )

    evaluator = Evaluator(config)
    results = evaluator.run_evaluation(full_evaluation=full, quick_validation=quick)

    # Get quality gate thresholds from config
    quality_config = config.get("quality", {})

    # Display results
    table = Table(title="Evaluation Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_column("Target", style="yellow")
    table.add_column("Status", style="bold")

    # Add metrics with config-based thresholds
    metrics = [
        (
            "Top-5 Relevance",
            results["top5_relevance"],
            quality_config.get("min_relevance_threshold", 0.85),
        ),
        (
            "P95 Latency (ms)",
            results["p95_latency"],
            quality_config.get("max_latency_threshold_ms", 500),
        ),
        ("MRR@10", results["mrr_at_10"], 0.7),
        (
            "Coverage",
            results["coverage"],
            quality_config.get("min_coverage_threshold", 0.90),
        ),
    ]

    all_passed = True
    for metric_name, value, target in metrics:
        if metric_name == "P95 Latency (ms)":
            status = "✓ PASS" if value <= target else "✗ FAIL"
            if value > target:
                all_passed = False
        else:
            status = "✓ PASS" if value >= target else "✗ FAIL"
            if value < target:
                all_passed = False
        status_color = "green" if "PASS" in status else "red"

        table.add_row(
            metric_name,
            f"{value:.3f}" if isinstance(value, float) else str(value),
            f"{target:.3f}" if isinstance(value, float) else str(target),
            f"[{status_color}]{status}[/{status_color}]",
        )

    console.print(table)

    # Quality gate summary
    gate_color = "green" if all_passed else "red"
    gate_status = "✅ QUALITY GATE PASSED" if all_passed else "❌ QUALITY GATE FAILED"
    console.print(f"\n[{gate_color}]{gate_status}[/{gate_color}]")

    # Show failed queries if any
    if results.get("failed_queries"):
        console.print("\n[yellow]Failed queries:[/yellow]")
        for query in results["failed_queries"]:
            console.print(f"  - {query}")

    # Exit with appropriate code for CI/CD integration
    if not all_passed:
        sys.exit(1)


@cli.command()
@click.option(
    "--debounce", type=int, default=3, help="Seconds to debounce rapid changes"
)
@click.option("--once", is_flag=True, help="Run one incremental index pass and exit")
@click.option("--verbose", "-v", is_flag=True, help="Verbose logging")
@click.pass_context
def watch(ctx, debounce, once, verbose):
    """Automatically index on memory-bank changes.

    Watches the memory bank directory and runs incremental indexing when files change.
    """
    try:
        from watchfiles import watch
    except Exception as e:
        console.print(f"[red]watchfiles not available: {e}[/red]")
        console.print("Install with: pip install watchfiles")
        sys.exit(1)

    config = ctx.obj["config"]
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    memory_bank_root = Path(config["storage"]["memory_bank_root"])
    if not memory_bank_root.exists():
        console.print(f"[red]Memory bank path not found:[/red] {memory_bank_root}")
        sys.exit(1)

    # Initialize components once and reuse
    chunker = MemoryBankChunker(config)
    embedder = LocalEmbedder(config)
    searcher = HybridSearcher(config, embedder)
    searcher.create_or_load_collection()
    indexer = IncrementalIndexer(config, chunker, embedder, searcher)

    def run_incremental():
        console.print("[yellow]Checking for changes...[/yellow]")
        count = indexer.incremental_index()
        if count:
            console.print(f"[green]✓ Indexed {count} changed file(s)[/green]")
        else:
            console.print("[dim]No changes[/dim]")

    # Initial pass
    run_incremental()
    if once:
        return

    console.print(
        Panel.fit(
            f"[bold cyan]MBIE Watch[/bold cyan]\nWatching {memory_bank_root} for changes...\nDebounce: {debounce}s"
        )
    )

    last_run_ts = 0.0
    for _changes in watch(str(memory_bank_root)):
        now = time.time()
        if now - last_run_ts < debounce:
            continue
        last_run_ts = now
        run_incremental()


def main():
    """Main entry point"""
    cli(obj={})


if __name__ == "__main__":
    main()
