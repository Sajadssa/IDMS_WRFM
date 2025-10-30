# IDMS WRFM - Integrated Document Management System with Workflow & RFI Management

A comprehensive system for managing construction project documents, workflows, and RFI (Request for Information) processes.

## 🏗️ Project Status

**Current Phase**: Phase 2 - Backend Development (40% Complete)  
**Last Completed**: Task 2.2 - FastAPI Structure  
**Next Task**: Task 2.3 - Database Models

---

##  Completed Features

### Phase 0: Setup (100% Complete)
-  Project initialization
- ✅ Git repository setup
- ✅ Directory structure created

### Phase 1: Infrastructure (100% Complete)
- ✅ **Docker PostgreSQL** - Running on port 5432
- ✅ **Docker Redis** - Running on port 6379
- ✅ **Database Initialization** - idms_wrfm database created
- ✅ **Infrastructure Verification** - All services tested and operational

### Phase 2: Backend (40% Complete)
-  **Backend Setup**
  - Python virtual environment configured
  - All dependencies installed (FastAPI, SQLAlchemy 2.0, etc.)
  - Backend directory structure initialized

-  **Core Configuration**
  - Pydantic Settings implementation
  - .env file configuration
  - Database URL management
  - Redis URL management
  - JWT secret configuration
  - Environment validation

-  **FastAPI Structure**
  - Main FastAPI application (ackend/app/main.py)
  - API v1 router structure (ackend/app/api/v1/)
  - Health check endpoints (basic & detailed)
  - Placeholder endpoints (auth, projects, rfis)
  - Custom logging middleware
  - Database session management
  - CORS middleware configuration
  - Trusted hosts security
  - Development server runner (ackend/run.py)

---

##  Current API Endpoints

### Root & Health
- GET / - Root endpoint with welcome message
- GET /health - Basic health check

### API v1
- GET /api/v1/health/detailed - Detailed health check (includes DB connection test)

### Authentication (Placeholders)
- POST /api/v1/auth/login
- POST /api/v1/auth/register
- POST /api/v1/auth/logout
- GET /api/v1/auth/me

### Projects (Placeholders)
- GET /api/v1/projects/
- GET /api/v1/projects/{project_id}

### RFIs (Placeholders)
- GET /api/v1/rfis/
- GET /api/v1/rfis/{rfi_id}

---

## 📚 API Documentation

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

---

##  Tech Stack

### Backend
- **Framework**: FastAPI 0.115.5
- **ORM**: SQLAlchemy 2.0.36
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Authentication**: JWT (python-jose)
- **Password Hashing**: passlib with bcrypt
- **Migrations**: Alembic
- **Validation**: Pydantic 2.10.3

### Frontend (Planned)
- Next.js 14
- TypeScript
- Tailwind CSS
- shadcn/ui components

### Infrastructure
- Docker & Docker Compose
- Git version control

---

##  Installation & Setup

### Prerequisites
- Python 3.11+
- Docker Desktop
- Git
- Node.js 18+ (for frontend, later)

### Quick Start

1. **Clone the repository**
\\\powershell
git clone <repository-url>
cd IDMS_WRFM
\\\

2. **Run setup script**
\\\powershell
.\scripts\setup.sh
\\\

3. **Activate virtual environment**
\\\powershell
.\backend\venv\Scripts\Activate.ps1
\\\

4. **Start the backend server**
\\\powershell
python backend\run.py
\\\

5. **Access the API**
- API Docs: http://localhost:8000/api/docs
- Health Check: http://localhost:8000/health

---

## 🗂️ Project Structure

\\\
IDMS_WRFM/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── config.py            # Pydantic settings
│   │   ├── database.py          # Database configuration
       api/
          v1/
              __init__.py
              router.py    # Main v1 router
              endpoints/   # Endpoint modules
       models/              # SQLAlchemy models (next task)
       schemas/             # Pydantic schemas
       services/            # Business logic
       middleware/          # Custom middleware
    run.py                   # Development server
    requirements.txt         # Python dependencies
    venv/                    # Virtual environment
 frontend/                    # Next.js app (planned)
├── scripts/
│   └── setup.sh                 # Infrastructure setup script
 .env                         # Environment variables
 .gitignore
 docker-compose.yml           # PostgreSQL & Redis
 TODO.md                      # Development checklist
 README.md                    # This file
\\\

---

##  Environment Variables

Create a .env file in the project root:

\\\env
# Database
DATABASE_URL=postgresql://idms_user:idms_secure_password_2024@localhost:5432/idms_wrfm

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App
PROJECT_NAME=IDMS WRFM
VERSION=1.0.0
DEBUG=true
\\\

---

##  Next Steps

### Immediate (Task 2.3 - Database Models)
1. Create base model class with common fields
2. Implement User model for authentication
3. Implement Project model
4. Implement RFI model with relationships
5. Setup Alembic migrations

### Upcoming (Phase 2 - Backend)
- Task 2.4: Authentication System (JWT, password hashing)
- Task 2.5: API Endpoints (CRUD operations)
- Task 2.6: Testing (pytest, test coverage)

---

##  Development Notes

### Middleware Stack
1. **Logging Middleware** - Request/response logging with timing
2. **CORS Middleware** - Cross-origin resource sharing
3. **Trusted Hosts** - Security for allowed hosts

### Database Session Management
- Dependency injection pattern
- Automatic session cleanup
- Connection pooling via SQLAlchemy

### Error Handling
- Custom logging for all requests
- Detailed health checks with DB connection testing
- Proper HTTP status codes

---

##  Contributing

1. Follow the task checklist in TODO.md
2. Update documentation after each task
3. Commit with descriptive messages
4. Test all changes before committing

---

##  License

[Your License Here]

---

**Last Updated**: 2025-10-31 (1404/08/09)  
**Version**: 1.0.0  
**Maintained By**: Sepher Pasargad Development Team
