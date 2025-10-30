#!/bin/bash
# Setup script for RFI Management System

echo " Setting up RFI Management System..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    
    # Generate secret key
    if command -v python3 &> /dev/null; then
        SECRET_KEY=$(python3 scripts/generate_secret.py)
        sed -i "s/your-secret-key-here-generate-with-scripts\/generate_secret.py/$SECRET_KEY/" .env
        echo " Secret key generated"
    else
        echo "  Python3 not found. Please generate SECRET_KEY manually."
    fi
fi

# Create necessary directories
mkdir -p postgres/init
mkdir -p backend/app
mkdir -p frontend/src

echo " Setup complete!"
echo ""
echo "Next steps:"
echo "1. Review and update .env file"
echo "2. Run: docker compose up -d"
echo "3. Access application at http://localhost"
