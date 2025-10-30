#!/bin/bash

echo "🔍 Checking IDMS_WRFM Setup..."
echo "================================"

# Check Docker
if command -v docker &> /dev/null; then
    echo "✅ Docker installed: $(docker --version)"
else
    echo "❌ Docker not installed"
    exit 1
fi

# Check Docker Compose
if command -v docker-compose &> /dev/null; then
    echo "✅ Docker Compose installed: $(docker-compose --version)"
else
    echo "❌ Docker Compose not installed"
    exit 1
fi

# Check .env file
if [ -f .env ]; then
    echo "✅ .env file exists"
else
    echo "⚠️  .env file not found. Copy from .env.example"
fi

# Check folder structure
REQUIRED_DIRS=("backend" "frontend" "nginx" "docs" "scripts")
for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ Directory exists: $dir"
    else
        echo "❌ Directory missing: $dir"
    fi
done

echo "================================"
echo "✅ Setup check complete!"
