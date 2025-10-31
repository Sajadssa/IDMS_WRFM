# IDMS WRFM - Integrated Document Management System with Workflow & RFI Management

A comprehensive system for managing construction project documents, workflows, and RFI (Request for Information) processes.

##  Project Status

**Current Phase**: Phase 2 - Backend Development (80% Complete)  
**Last Completed**: Task 2.4 - Authentication System  
**Next Task**: Task 2.5 - API Endpoints (CRUD Operations)

---

##  Completed Features

### Phase 0: Setup (100% Complete)
-  Project initialization
-  Git repository setup
-  Directory structure created

### Phase 1: Infrastructure (100% Complete)
-  **Docker PostgreSQL** - Running on port 5432
-  **Docker Redis** - Running on port 6379
-  **Database Initialization** - `idms_wrfm` database created
-  **Infrastructure Verification** - All services tested and operational

### Phase 2: Backend (80% Complete)
-  **Backend Setup** - Virtual environment, dependencies
-  **Core Configuration** - Pydantic settings, .env management
-  **FastAPI Structure** - Main app, routers, middleware, endpoints
-  **Database Configuration**
  - SQLAlchemy 2.0 base model with timestamps
  - User model (authentication ready)
  - Project model with status tracking
  - RFI model with priority and status
  - Alembic migrations configured
  - Database schema created and migrated

-  **Authentication System** (NEW!)
  - **Password Hashing**: bcrypt with passlib
  - **JWT Tokens**: Access (30 min) & Refresh (7 days)
  - **Security**: OAuth2PasswordBearer, token validation
  - **Pydantic Schemas**: User, Auth, Token models
  - **Auth Dependencies**: 
    - `get_current_user` - Extract user from JWT
    - `get_current_active_user` - Verify active status
    - `get_current_superuser` - Admin-only routes
  - **Endpoints**:
    - `POST /api/v1/auth/register` - User registration
    - `POST /api/v1/auth/login` - Login with username/password
    - `POST /api/v1/auth/logout` - Logout (client-side token removal)
    - `GET /api/v1/auth/me` - Get current user info
    - `POST /api/v1/auth/refresh` - Refresh access token

---

##  Database Schema

### User Model
- `id` (Primary Key)
- `username` (Unique, Indexed)
- `email` (Unique, Indexed)
- `hashed_password` (bcrypt)
- `full_name`
- `is_active`, `is_superuser` (Booleans)
- `created_at`, `updated_at` (Timestamps)

### Project Model
- `id` (Primary Key)
- `name`, `project_code` (Unique, Indexed)
- `description`
- `status` (Enum: planning, active, on_hold, completed, cancelled)
- `owner_id` (Foreign Key  User)
- `created_at`, `updated_at`

### RFI Model
- `id` (Primary Key)
- `rfi_number` (Unique, Indexed)
- `subject`, `description`
- `status` (Enum: draft, submitted, in_review, answered, closed, cancelled)
- `priority` (Enum: low, medium, high, urgent)
- `due_date`, `response`
- `project_id` (Foreign Key  Project)
- `creator_id` (Foreign Key  User)
- `created_at`, `updated_at`

### Relationships
- User  Projects (One-to-Many)
- User  RFIs (One-to-Many)
- Project  RFIs (One-to-Many)

---

##  Authentication Flow

### Registration
\\\ash
POST /api/v1/auth/register
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123",
  "full_name": "John Doe"
}
\\\

### Login
\\\ash
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "john_doe",
  "password": "SecurePass123"
}

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    ...
  }
}
\\\

### Protected Routes
\\\ash
GET /api/v1/auth/me
Authorization: Bearer <access_token>

Response:
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2025-10-31T...",
  "updated_at": "2025-10-31T..."
}
\\\

---

##  Current API Endpoints

### Root & Health
- `GET /` - Root endpoint
- `GET /health` - Basic health check
- `GET /api/v1/health/detailed` - Detailed health (includes DB connection)

### Authentication 
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login (returns JWT tokens)
- `POST /api/v1/auth/logout` - Logout
- `GET /api/v1/auth/me` - Get current user (requires auth)
- `POST /api/v1/auth/refresh` - Refresh access token

### Projects (Placeholders  Next Task)
- `GET /api/v1/projects/`
- `GET /api/v1/projects/{project_id}`

### RFIs (Placeholders  Next Task)
- `GET /api/v1/rfis/`
- `GET /api/v1/rfis/{rfi_id}`

---

##  API Documentation

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

---

### ============================================
# ادامه اسکریپت Task 2.4 - قسمت دوم
# ============================================

##  Project Structure

\\\
IDMS_WRFM/

 backend/
    app/
       __init__.py
       main.py                  # FastAPI application
       run.py                   # Development runner
      
       api/                     # API endpoints
          __init__.py
          v1/
              __init__.py
              api.py           # Router aggregator
              endpoints/
                  __init__.py
                  health.py    #  Health checks
                  auth.py      #  Authentication
                  projects.py  #  Project CRUD (next)
                  rfis.py      #  RFI CRUD (next)
      
       core/                    # Core utilities
          __init__.py
          config.py            #  Settings
          security.py          #  Password & JWT
          dependencies.py      #  Auth dependencies
      
       db/                      # Database
          __init__.py
          base.py              #  Base model
          session.py           #  Database session
      
       models/                  # SQLAlchemy models
          __init__.py
          user.py              #  User model
          project.py           #  Project model
          rfi.py               #  RFI model
      
       schemas/                 # Pydantic schemas
          __init__.py
          user.py              #  User schemas
          auth.py              #  Auth schemas
      
       middleware/              # Custom middleware
           __init__.py
           logging.py           #  Logging middleware
   
    alembic/                     #  Database migrations
       versions/
       env.py
       alembic.ini
   
    tests/                       # Test suite
       __init__.py
   
    requirements.txt             #  Dependencies
    requirements-dev.txt         #  Dev dependencies
    requirements-prod.txt        #  Production dependencies

 frontend/                        #  Next.js (Phase 3)
    (to be implemented)

 scripts/                         # Utility scripts
    install-deps.sh              #  Dependency installer

 .env                            #  Environment variables
 .gitignore                      #  Git ignore
 docker-compose.yml              #  Docker services
 setup.sh                        #  Project setup script
 README.md                       #  This file
 TODO.md                         #  Progress tracker
\\\

---

##  Tech Stack

### Backend
- **Framework**: FastAPI 0.115.0
- **Database**: PostgreSQL 17 (via Docker)
- **ORM**: SQLAlchemy 2.0.35
- **Cache**: Redis 5.1.1 (via Docker)
- **Authentication**: JWT (python-jose) + bcrypt (passlib)
- **Validation**: Pydantic 2.9.0
- **Migrations**: Alembic 1.13.2
- **ASGI Server**: Uvicorn 0.32.0

### Frontend (Planned)
- Next.js 14+
- TypeScript
- TailwindCSS
- React Query

### Infrastructure
- Docker & Docker Compose
- PostgreSQL 17
- Redis 7

---

##  Quick Start

### 1. Prerequisites
\\\ash
# Required
- Python 3.11+
- Docker & Docker Compose
- Git

# Optional
- Node.js 18+ (for frontend)
\\\

### 2. Clone Repository
\\\ash
git clone <repository-url>
cd IDMS_WRFM
\\\

### 3. Run Setup Script
\\\ash
# Linux/Mac
chmod +x setup.sh
./setup.sh

# Windows (PowerShell)
.\setup.ps1
\\\

This script will:
- Create directory structure
- Set up Python virtual environment
- Install dependencies
- Start Docker containers (PostgreSQL + Redis)
- Run database migrations
- Create initial superuser

### 4. Manual Setup (Alternative)

#### Start Docker Services
\\\ash
docker-compose up -d
\\\

#### Setup Python Environment
\\\ash
cd backend
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
\\\

#### Run Database Migrations
\\\ash
cd backend
alembic upgrade head
\\\

#### Start Backend Server
\\\ash
cd backend
python -m app.run

# Or directly with uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
\\\

---

##  Database Migrations

### Create New Migration
\\\ash
cd backend
alembic revision --autogenerate -m "description of changes"
\\\

### Apply Migrations
\\\ash
alembic upgrade head
\\\

### Rollback Migration
\\\ash
alembic downgrade -1
\\\

### View Migration History
\\\ash
alembic history
\\\

---

##  Configuration

### Environment Variables (.env)
\\\env
# Application
APP_NAME=IDMS WRFM
DEBUG=True

# Database
DATABASE_URL=postgresql://idms_user:idms_password@localhost:5432/idms_wrfm

# Redis
REDIS_URL=redis://localhost:6379/0

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
CORS_ORIGINS=["http://localhost:3000"]
\\\

---

##  Development Progress

- **Phase 0** (Setup):  100%
- **Phase 1** (Infrastructure):  100%
- **Phase 2** (Backend):  80%
- **Phase 3** (Frontend):  0%
- **Phase 4** (Deployment):  0%

**Overall Progress**: 45%

---

##  Next Steps

1.  **Task 2.5**: Implement CRUD Endpoints
   - Project management endpoints
   - RFI management endpoints
   - File upload handling

2.  **Task 2.6**: Backend Testing
   - Unit tests for models
   - Integration tests for APIs
   - Auth flow testing

3.  **Phase 3**: Frontend Development
   - Next.js setup
   - Authentication UI
   - Dashboard implementation

---

##  Git Workflow

### Current Branch
\\\ash
main (or development)
\\\

### Commit Convention
\\\
feat: Add new feature
fix: Bug fix
docs: Documentation update
test: Add tests
refactor: Code refactoring
chore: Maintenance tasks
\\\

---

##  Contributing

1. Fork the repository
2. Create feature branch (\git checkout -b feature/AmazingFeature\)
3. Commit changes (\git commit -m 'feat: Add amazing feature'\)
4. Push to branch (\git push origin feature/AmazingFeature\)
5. Open Pull Request

---

##  License

This project is proprietary software for Sepher Pasargad.

---

##  Contact

Project Link: [Repository URL]

---

**Last Updated**: 2025-10-31 (Task 2.4 - Authentication System Completed)

