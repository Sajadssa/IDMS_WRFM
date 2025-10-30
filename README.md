# IDMS WRFM - Integrated Document Management System with Workflow & RFI Management

A comprehensive system for managing construction project documents, workflows, and RFI (Request for Information) processes.

##  Project Status

**Current Phase**: Phase 2 - Backend Development (60% Complete)  
**Last Completed**: Task 2.3 - Database Configuration  
**Next Task**: Task 2.4 - Authentication System

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

### Phase 2: Backend (60% Complete)
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

---

##  Database Schema

### User Model
- `id` (Primary Key)
- `username` (Unique, Indexed)
- `email` (Unique, Indexed)
- `hashed_password`
- `full_name`
- `is_active`, `is_superuser` (Booleans)
- `created_at`, `updated_at` (Timestamps)

### Project Model
- `id` (Primary Key)
- `name`, `project_code` (Unique, Indexed)
- `description`
- `status` (Enum: planning, active, on_hold, completed, cancelled)
- `owner_id` (Foreign Key → User)
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

##  Current API Endpoints

### Root & Health
- `GET /` - Root endpoint
- `GET /health` - Basic health check
- `GET /api/v1/health/detailed` - Detailed health (includes DB connection)

### Authentication (Placeholders)
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/logout`
- `GET /api/v1/auth/me`

### Projects (Placeholders)
- `GET /api/v1/projects/`
- `GET /api/v1/projects/{project_id}`

### RFIs (Placeholders)
- `GET /api/v1/rfis/`
- `GET /api/v1/rfis/{rfi_id}`

---

##  API Documentation

- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

---

##  Tech Stack

### Backend
- **Framework**: FastAPI 0.115.5
- **ORM**: SQLAlchemy 2.0.36
- **Migrations**: Alembic 1.14.0
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Authentication**: JWT (python-jose)
- **Password Hashing**: passlib with bcrypt
- **Validation**: Pydantic 2.10.3

### Database Models
- Base model with automatic timestamps
- Enum support for status fields
- Relationship management with cascade delete
- Auto-generated table names

---

## 📦 Installation & Setup

### Quick Start

1. **Clone and setup**
\\\powershell
git clone <repository-url>
cd IDMS_WRFM
.\scripts\setup.sh
\\\

2. **Activate environment**
\\\powershell
.\backend\venv\Scripts\Activate.ps1
\\\

3. **Run migrations** (if needed)
\\\powershell
cd backend
alembic upgrade head
\\\

4. **Start server**
\\\powershell
python backend\run.py
\\\

---

##  Project Structure

\\\
IDMS_WRFM/
 backend/
    app/
       main.py
       config.py
      ├── database.py
│   │   ├── api/v1/
│   │   ├── models/
          __init__.py
          base.py        # Base model with timestamps
          user.py        # User authentication model
│   │   │   ├── project.py     # Project management model
│   │   │   └── rfi.py         # RFI model with enums
       schemas/           # Pydantic schemas (next)
       services/          # Business logic (next)
    alembic/               # Database migrations
       versions/          # Migration files
       env.py             # Alembic configuration
    requirements.txt
├── scripts/
├── .env
├── docker-compose.yml
 README.md
\\\

---

##  Database Migrations

### Create new migration
\\\powershell
cd backend
alembic revision --autogenerate -m "Description"
\\\

### Apply migrations
\\\powershell
alembic upgrade head
\\\

### Rollback migration
\\\powershell
alembic downgrade -1
\\\

### View migration history
\\\powershell
alembic history
\\\

---

##  Next Steps

### Immediate (Task 2.4 - Authentication System)
1. Create password hashing utilities
2. Implement JWT token generation/validation
3. Create auth dependencies (get_current_user)
4. Implement login endpoint
5. Implement register endpoint

---

**Last Updated**: 2025-10-31 (1404/08/09)  
**Version**: 1.0.0  
**Maintained By**: Sepher Pasargad Development Team
