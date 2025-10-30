#!/bin/bash

# ============================================
# IDMS WRFM - Setup Script
# ============================================

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Helper Functions
print_header() {
    echo -e "\n${CYAN}============================================${NC}"
    echo -e "${CYAN}$1${NC}"
    echo -e "${CYAN}============================================${NC}\n"
}

print_step() {
    echo -e "${BLUE} $1${NC}"
}

print_success() {
    echo -e "${GREEN} $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

check_command() {
    if command -v $1 &> /dev/null; then
        print_success "$1 is installed"
        return 0
    else
        print_error "$1 is not installed"
        return 1
    fi
}

# ============================================
# Main Setup
# ============================================

print_header "IDMS WRFM - Project Setup"

# Check Prerequisites
print_header "Checking Prerequisites"
PREREQUISITES_OK=true

print_step "Checking Python..."
if check_command python3; then
    python3 --version
else
    PREREQUISITES_OK=false
fi

print_step "Checking Docker..."
if check_command docker; then
    docker --version
else
    PREREQUISITES_OK=false
fi

print_step "Checking Docker Compose..."
if check_command docker-compose; then
    docker-compose --version
else
    PREREQUISITES_OK=false
fi

print_step "Checking Git..."
if check_command git; then
    git --version
else
    PREREQUISITES_OK=false
fi

if [ "$PREREQUISITES_OK" = false ]; then
    print_error "Some prerequisites are missing"
    exit 1
fi

# Environment Setup
print_header "Setting Up Environment"

print_step "Checking .env file..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_success ".env file created"
    else
        print_error ".env.example not found"
        exit 1
    fi
else
    print_success ".env file exists"
fi

# Docker Services
print_header "Starting Docker Services"
docker-compose up -d
sleep 5
print_success "Docker services started"

# Python Environment
print_header "Setting Up Python Environment"

if [ ! -d "venv" ]; then
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_warning "Virtual environment exists"
fi

source venv/bin/activate
pip install --upgrade pip > /dev/null 2>&1
print_success "pip upgraded"

# Backend Dependencies
print_header "Installing Backend Dependencies"
cd backend
pip install -r requirements.txt
print_success "Dependencies installed"

# Database Migration
print_header "Database Setup"
alembic upgrade head
print_success "Migrations completed"

cd ..

# Complete
print_header "Setup Complete! "
echo -e "${GREEN}Next steps:${NC}"
echo -e "  1. source venv/bin/activate"
echo -e "  2. cd backend && python run.py"
echo -e "  3. Visit: http://localhost:8000/docs"
