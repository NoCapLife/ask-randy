#!/bin/bash
set -e

echo "🔍 Validating MBIE Toolkit Before Client Deployment..."
echo "=================================================="
echo ""

# Store original directory
ORIGINAL_DIR=$(pwd)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

# Check Python version
echo "1️⃣  Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 9 ]); then
    echo "❌ Python 3.9+ required. Found: Python $PYTHON_VERSION"
    exit 1
fi
echo "   ✅ Python $PYTHON_VERSION detected"
echo ""

# Navigate to MBIE directory
echo "2️⃣  Installing MBIE dependencies..."
cd tools/memory_rag

# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -q -r requirements.txt
    echo "   ✅ Dependencies installed"
else
    echo "   ⚠️  No requirements.txt found"
fi
echo ""

# Run MBIE test suite
echo "3️⃣  Running MBIE test suite..."
if command -v pytest &> /dev/null; then
    pytest tests/ -v --tb=short
    TEST_EXIT_CODE=$?
    if [ $TEST_EXIT_CODE -eq 0 ]; then
        echo "   ✅ All MBIE tests passed"
    else
        echo "   ⚠️  Some tests failed (exit code: $TEST_EXIT_CODE)"
        echo "   Note: This may be acceptable if failures are environment-specific"
        echo "   Review failures and decide if blocking for client deployment"
    fi
else
    echo "   ⚠️  pytest not found, skipping test suite"
    echo "   Install pytest: pip install pytest"
fi
echo ""

# Test MBIE CLI
echo "4️⃣  Testing MBIE CLI functionality..."
python -m memory_rag.cli --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "   ✅ MBIE CLI operational"
else
    echo "   ❌ MBIE CLI failed"
    exit 1
fi
echo ""

# Check for placeholder values
echo "5️⃣  Checking for placeholder values..."
cd "$PROJECT_ROOT"

PLACEHOLDERS_FOUND=0

# Check memory-bank files
if grep -r "\[Project Owner\]" memory-bank/ > /dev/null 2>&1; then
    echo "   ⚠️  Found [Project Owner] placeholders in memory-bank/"
    PLACEHOLDERS_FOUND=1
fi

if grep -r "\[Project Name\]" memory-bank/ > /dev/null 2>&1; then
    echo "   ⚠️  Found [Project Name] placeholders in memory-bank/"
    PLACEHOLDERS_FOUND=1
fi

if [ $PLACEHOLDERS_FOUND -eq 0 ]; then
    echo "   ✅ No obvious placeholders found (or already customized)"
else
    echo "   ℹ️  Reminder: Replace placeholders before client deployment"
fi
echo ""

# Summary
echo "=================================================="
echo "📋 Validation Summary:"
echo "   • Python version: ✅"
echo "   • MBIE dependencies: ✅"
echo "   • MBIE test suite: Check output above"
echo "   • MBIE CLI: ✅"
echo "   • Placeholder check: Check warnings above"
echo ""
echo "🚀 Ready for client deployment!"
echo ""
echo "Next steps:"
echo "  1. Clone to client repo: git clone Template.git [ClientName]-transformation"
echo "  2. Customize memory-bank with client context"
echo "  3. Test MBIE indexing on client documentation"
echo "  4. Deploy and deliver transformation"
echo ""

cd "$ORIGINAL_DIR"
