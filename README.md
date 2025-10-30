#  IDMS_WRFM - Intelligent Document Management System

**Workflow & RFI Management System**

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7-red?logo=redis)](https://redis.io/)
[![Python](https://img.shields.io/badge/Python-3.11+-yellow?logo=python)](https://www.python.org/)

---

##  Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development](#development)
- [Documentation](#documentation)
- [Contributing](#contributing)

---

##  Overview

IDMS_WRFM is a comprehensive Document Management System designed for managing Requests for Information (RFI) in construction and engineering projects. The system provides workflow automation, document tracking, and collaborative features.

### Key Capabilities
- 📝 **RFI Management**: Create, track, and manage RFIs throughout their lifecycle
- 🔄 **Workflow Automation**: Automated routing and approval processes
-  **Multi-user Collaboration**: Role-based access control and team collaboration
-  **Analytics & Reporting**: Project insights and performance metrics
-  **Advanced Search**: Full-text search and filtering capabilities
-  **Document Storage**: Secure file upload and management

---

##  Features

### Current Implementation (Phase 1-2)
-  Docker-based infrastructure
-  PostgreSQL database with health monitoring
-  Redis caching layer
-  FastAPI backend foundation
-  Multi-stage Docker builds
-  Development and production environments

### Planned Features
-  User authentication and authorization (JWT)
-  RFI creation and management
-  Project management
-  File upload and processing
-  Email notifications
-  Real-time updates
-  Reporting and analytics

---

##  Architecture

### Docker-First Strategy
The project follows a **Docker-First** approach:
- All services run in Docker containers
- Development environment mirrors production
- Easy setup and consistent environments
- Scalable and maintainable

### System Components

\\\

           Load Balancer/Nginx           

              
    
                       
        
Backend  Redis   
FastAPI          Cache   
        
    

PostgreSQL
 Database 

\\\

---

##  Tech Stack

### Backend
- **Framework**: FastAPI 0.115.0
- **Language**: Python 3.11+
- **ORM**: SQLAlchemy 2.0.35
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt

### DevOps & Infrastructure
- **Containerization**: Docker & Docker Compose
- **Migration Tool**: Alembic
- **Web Server**: Uvicorn (ASGI)
- **Monitoring**: Prometheus

### Development Tools
- **Testing**: pytest, pytest-asyncio
- **Code Quality**: black, flake8, mypy, isort
- **Documentation**: mkdocs, mkdocs-material

---

##  Getting Started

### Prerequisites
- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Docker Compose V2
- Git
- 4GB RAM minimum
- 10GB free disk space

### Quick Start

\\\powershell
# 1. Clone the repository
git clone <repository-url>
cd IDMS_WRFM

# 2. Run setup script
./scripts/setup.sh

# 3. Start services
docker compose up -d

# 4. Check health
./scripts/health_check.sh

# 5. Access the application
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
\\\

### Environment Setup

Copy the example environment file and configure:
\\\powershell
cp .env.example .env
# Edit .env with your settings
\\\

**Important**: Never commit the \.env\ file!

---

##  Project Structure

\\\
IDMS_WRFM/
 backend/                    # FastAPI backend
    app/                   # Application code
       api/              # API endpoints
       core/             # Core configuration
       models/           # Database models
       schemas/          # Pydantic schemas
       services/         # Business logic
       main.py           # Application entry point
    tests/                 # Backend tests
    alembic/              # Database migrations
    Dockerfile            # Production build
    Dockerfile.dev        # Development build
    requirements.txt      # All dependencies
    requirements-dev.txt  # Dev dependencies
    requirements-prod.txt # Production dependencies

 frontend/                  # Next.js frontend (planned)

 scripts/                   # Utility scripts
    setup.sh              # Initial setup
    health_check.sh       # Health monitoring
    build-backend.sh      # Backend build
    install-deps.sh       # Dependency installation

 docs/                      # Project documentation
    WBS/                  # Work Breakdown Structure
    architecture/         # Architecture diagrams
    api/                  # API documentation

 .github/                   # GitHub workflows (planned)
 docker-compose.yml        # Docker services definition
 .env.example              # Environment template
 .gitignore               # Git ignore rules
 TODO.md                  # Task tracking
 README.md                # This file
\\\

---

##  Development

### Running Development Environment

\\\powershell
# Start all services
docker compose up -d

# View logs
docker compose logs -f backend

# Run tests
docker compose exec backend pytest

# Code formatting
docker compose exec backend black .

# Type checking
docker compose exec backend mypy .

# Stop services
docker compose down
\\\

### Database Operations

\\\powershell
# Create new migration
docker compose exec backend alembic revision --autogenerate -m "description"

# Apply migrations
docker compose exec backend alembic upgrade head

# Rollback migration
docker compose exec backend alembic downgrade -1

# View migration history
docker compose exec backend alembic history
\\\

### Installing Dependencies

\\\powershell
# Install production dependencies
./scripts/install-deps.sh prod

# Install development dependencies
./scripts/install-deps.sh dev

# Install all dependencies
./scripts/install-deps.sh
\\\

---

##  Documentation

- **API Documentation**: Available at \http://localhost:8000/docs\ (Swagger UI)
- **Alternative API Docs**: \http://localhost:8000/redoc\ (ReDoc)
- **WBS**: See \docs/WBS/\ for detailed task breakdown
- **Architecture**: See \docs/architecture/\ for system design

---

##  Testing

\\\powershell
# Run all tests
docker compose exec backend pytest

# Run with coverage
docker compose exec backend pytest --cov=app --cov-report=html

# Run specific test file
docker compose exec backend pytest tests/test_users.py

# Run tests with output
docker compose exec backend pytest -v -s
\\\

---

##  Security

- JWT-based authentication
- Bcrypt password hashing
- CORS configuration
- Environment variable protection
- SQL injection prevention (SQLAlchemy ORM)
- Input validation (Pydantic)

---

##  Current Status

### Completed (Phase 0-2.1)
-  Project initialization and Git setup
-  Docker infrastructure (Postgres, Redis)
-  Backend foundation (FastAPI)
-  Multi-stage Docker builds
-  Requirements management
-  Health checks and monitoring

### In Progress (Phase 2.2)
-  Database models (User, Project, RFI)

### Next Steps
- Database connection and configuration
- Alembic migrations
- Authentication system
- API endpoints
- Frontend development

**Overall Progress**: ~25% Complete

---

##  Contributing

1. Fork the repository
2. Create a feature branch (\git checkout -b feature/amazing-feature\)
3. Commit your changes (\git commit -m 'Add amazing feature'\)
4. Push to the branch (\git push origin feature/amazing-feature\)
5. Open a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Use Black for formatting
- Type hints required
- Docstrings for all functions
- Tests for new features

---

##  License

This project is proprietary and confidential.

---

##  Team

- **Project Lead**: [Your Name]
- **Backend Developer**: [Name]
- **Frontend Developer**: [Name]
- **DevOps Engineer**: [Name]

---

##  Support

For issues and questions:
- Create an issue on GitHub
- Contact: [your-email@example.com]

---

##  Acknowledgments

- FastAPI framework by Sebastián Ramírez
- SQLAlchemy ORM
- Docker containerization
- PostgreSQL database
- Redis caching

---

**Last Updated**: 2025-10-31
**Version**: 0.2.1 (Phase 2 - Backend Foundation)
