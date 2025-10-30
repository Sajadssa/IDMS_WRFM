#!/bin/bash
# Install Python dependencies

echo "=== Installing Backend Dependencies ==="

# Check environment
if [ "$1" == "prod" ]; then
    echo " Installing production dependencies..."
    pip install -r backend/requirements-prod.txt
elif [ "$1" == "dev" ]; then
    echo "  Installing development dependencies..."
    pip install -r backend/requirements-dev.txt
else
    echo " Installing all dependencies..."
    pip install -r backend/requirements.txt
fi

echo "✅ Dependencies installed successfully!"
pip list
