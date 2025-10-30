#!/bin/bash
# ============================================
# IDMS_WRFM Setup Script
# Initializes development environment
# ============================================

set -e  # Exit on error

echo ""
echo "   IDMS_WRFM Development Setup          "
echo ""
echo ""

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# ============================================
# 1. Check Prerequisites
# ============================================
echo -e "${CYAN} Checking prerequisites...${NC}"

# Check Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed${NC}"
    echo "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
fi
echo -e "${GREEN} Docker installed${NC}"

# Check Docker Compose
if ! docker compose version &> /dev/null; then
    echo -e "${RED} Docker Compose V2 is not installed${NC}"
    exit 1
fi
echo -e "${GREEN} Docker Compose V2 installed${NC}"

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker is not running${NC}"
    echo "Please start Docker Desktop"
    exit 1
fi
echo -e "${GREEN}✅ Docker is running${NC}"

# ============================================
# 2. Create Directory Structure
# ============================================
echo -e "\n${CYAN} Creating directory structure...${NC}"

directories=(
    "backend/app/api/v1/endpoints"
    "backend/app/core"
    "backend/app/models"
    "backend/app/schemas"
    "backend/app/services"
    "backend/app/utils"
    "backend/tests"
    "backend/alembic/versions"
    "frontend/src"
    "docs/WBS"
    "docs/architecture"
    "docs/api"
    "scripts"
    ".github/workflows"
)

for dir in "${directories[@]}"; do
    mkdir -p "$dir"
    echo -e "${GREEN}${NC} Created: $dir"
done

# ============================================
# 3. Environment Setup
# ============================================
echo -e "\n${CYAN} Setting up environment...${NC}"

if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
        echo -e "${GREEN} Created .env from .env.example${NC}"
        echo -e "${YELLOW}  Please edit .env and set your credentials${NC}"
    else
        echo -e "${RED}❌ .env.example not found${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  .env already exists, skipping...${NC}"
fi

# ============================================
# 4. Build Docker Images
# ============================================
echo -e "\n${CYAN} Building Docker images...${NC}"

docker compose build --no-cache
echo -e "${GREEN} Docker images built${NC}"

# ============================================
# 5. Start Services
# ============================================
echo -e "\n${CYAN} Starting services...${NC}"

docker compose up -d
echo -e "${GREEN} Services started${NC}"

# ============================================
# 6. Wait for Services
# ============================================
echo -e "\n${CYAN} Waiting for services to be healthy...${NC}"

# Wait for Postgres
max_attempts=30
attempt=0
until docker compose exec -T postgres pg_isready -U idms_user &> /dev/null; do
    attempt=$((attempt + 1))
    if [ $attempt -ge $max_attempts ]; then
        echo -e "${RED} Postgres failed to start${NC}"
        docker compose logs postgres
        exit 1
    fi
    echo -e "${YELLOW}Waiting for Postgres... ($attempt/$max_attempts)${NC}"
    sleep 2
done
echo -e "${GREEN} Postgres is ready${NC}"

# Wait for Redis
attempt=0
until docker compose exec -T redis redis-cli -a "${REDIS_PASSWORD:-idms_redis_password_2024}" ping &> /dev/null; do
    attempt=$((attempt + 1))
    if [ $attempt -ge $max_attempts ]; then
        echo -e "${RED} Redis failed to start${NC}"
        docker compose logs redis
        exit 1
    fi
    echo -e "${YELLOW}Waiting for Redis... ($attempt/$max_attempts)${NC}"
    sleep 2
done
echo -e "${GREEN}✅ Redis is ready${NC}"

# ============================================
# 7. Run Health Checks
# ============================================
echo -e "\n${CYAN} Running health checks...${NC}"

if [ -f scripts/health_check.sh ]; then
    bash scripts/health_check.sh
else
    echo -e "${YELLOW}  health_check.sh not found, skipping...${NC}"
fi

# ============================================
# 8. Display Summary
# ============================================
echo ""
echo ""
echo "         Setup Complete!               "
echo ""
echo ""
echo -e "${GREEN} IDMS_WRFM is ready for development!${NC}"
echo ""
echo "Services:"
echo -e "   Backend API:     ${CYAN}http://localhost:8000${NC}"
echo -e "   API Docs:        ${CYAN}http://localhost:8000/docs${NC}"
echo -e "   PostgreSQL:      ${CYAN}localhost:5432${NC}"
echo -e "   Redis:           ${CYAN}localhost:6379${NC}"
echo ""
echo "Next steps:"
echo "  1. Edit .env with your configuration"
echo "  2. docker compose up -d  # Start services"
echo "  3. docker compose logs -f  # View logs"
echo "  4. docker compose down  # Stop services"
echo ""
echo -e "${YELLOW} Check README.md for more information${NC}"
echo ""
