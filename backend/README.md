# IDMS WRFM - Integrated Document Management System & Workflow RFI Management

A comprehensive system for managing construction/engineering documents and RFI workflows.

---

##  Development Status

**Current Phase**: Phase 2 - Backend Development  
**Last Updated**: 2025-10-31  
**Overall Progress**: 50%

---

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
                  auth.py      #  Authentication (next)
                  projects.py  #  Project CRUD
                  rfis.py      #  RFI CRUD
      
       core/                    # Core utilities
          __init__.py
          config.py            #  Settings
          dependencies.py      #  Auth dependencies (next)
      
       db/                      # Database
          __init__.py
          base.py              #  Base models & mixins
          utils.py             #  CRUD utilities
          session.py           #  Database session
      
       models/                  # SQLAlchemy models
          __init__.py
          user.py              #  User model
          project.py           #  Project model
          rfi.py               #  RFI model
      
       schemas/                 # Pydantic schemas
          __init__.py
      
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

 scripts/                         # Utility# ============================================
# Step 9: Update README.md (continued)
# ============================================

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

**Last Updated**: 2025-10-31 (Task 2.4 - Authentication System Completed) = @"
# IDMS WRFM - Integrated Document Management System & Workflow RFI Management

A comprehensive system for managing construction/engineering documents and RFI workflows.

---

##  Development Status

**Current Phase**: Phase 2 - Backend Development  
**Last Updated**: 2025-10-31  
**Overall Progress**: 50%

---

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
                  auth.py      #  Authentication (next)
                  projects.py  #  Project CRUD
                  rfis.py      #  RFI CRUD
      
       core/                    # Core utilities
          __init__.py
          config.py            #  Settings
          dependencies.py      #  Auth dependencies (next)
      
       db/                      # Database
          __init__.py
          base.py              #  Base models & mixins
          utils.py             #  CRUD utilities
          session.py           #  Database session
      
       models/                  # SQLAlchemy models
          __init__.py
          user.py              #  User model
          project.py           #  Project model
          rfi.py               #  RFI model
      
       schemas/                 # Pydantic schemas
          __init__.py
      
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
    setup.sh                     #  Setup script

 docker-compose.yml               #  Docker services
 .env.example                     #  Environment template
 .gitignore                       #  Git ignore rules
 TODO.md                          #  Project checklist
 README.md                        #  This file
\\\

---

##  Technology Stack

### Backend
- **Framework**: FastAPI 0.115+
- **Language**: Python 3.12
- **Database**: PostgreSQL 17
- **ORM**: SQLAlchemy 2.0 (Async)
- **Migration**: Alembic
- **Cache**: Redis 7
- **Authentication**: JWT (PyJWT)
- **Validation**: Pydantic v2

### Frontend (Planned - Phase 3)
- **Framework**: Next.js 14
- **Language**: TypeScript
- **Styling**: TailwindCSS
- **State**: React Context / Zustand
- **API Client**: Axios / Fetch

### DevOps
- **Containerization**: Docker & Docker Compose
- **Web Server**: Uvicorn (dev) / Gunicorn + Uvicorn (prod)
- **Reverse Proxy**: Nginx (planned)
- **CI/CD**: GitHub Actions (planned)

---

##  Database Schema

### Base Model Features
All models inherit from **BaseModel** which provides:
- **Timestamps**: created_at, updated_at (automatic)
- **Serialization**: 	o_dict() method
- **Representation**: Enhanced __repr__()

### Available Mixins
- **TimestampMixin**: Automatic timestamp management
- **SoftDeleteMixin**: Soft delete with deleted_at, is_deleted, soft_delete(), estore()
- **UserTrackingMixin**: Track created_by_id and updated_by_id

### Models

####  User
\\\
users
 id (PK)
 username (unique, indexed)
 email (unique, indexed)
 hashed_password
 full_name
 is_active
 is_superuser
 created_at (auto)
 updated_at (auto)
\\\

**Relationships**:
- One-to-Many  Projects (as owner)
- One-to-Many  RFIs (as creator)
- One-to-Many  RFIs (as assignee)

---

####  Project
\\\
projects
 id (PK)
 name (indexed)
 code (unique, indexed)
 description
 status (enum: planning|active|on_hold|completed|cancelled)
 owner_id (FK  users.id)
 created_at (auto)
 updated_at (auto)
 deleted_at (soft delete)
\\\

**Features**:
- Soft delete support
- Status workflow management
- Unique project codes
- Cascade delete RFIs

**Relationships**:
- Many-to-One  User (owner)
- One-to-Many  RFIs

---

####  RFI (Request for Information)
\\\
rfis
 id (PK)
 title (indexed)
 rfi_number (unique, indexed)
 question
 response
 status (enum: draft|submitted|under_review|responded|closed|cancelled)
 priority (enum: low|medium|high|urgent)
 project_id (FK  projects.id)
 created_by_id (FK  users.id)
 assigned_to_id (FK  users.id)
 created_at (auto)
 updated_at (auto)
 deleted_at (soft delete)
\\\

**Features**:
- Soft delete support
- Priority levels
- Status workflow
- Question/Response tracking

**Relationships**:
- Many-to-One  Project
- Many-to-One  User (creator)
- Many-to-One  User (assignee)

---

##  Configuration

### Environment Variables
Create a .env file in the project root:

\\\env
# Database
DATABASE_URL=postgresql+asyncpg://idms_user:idms_pass@localhost:5432/idms_db

# Redis
REDIS_URL=redis://localhost:6379/0

# API
API_V1_PREFIX=/api/v1
PROJECT_NAME=IDMS WRFM

# Security (to be added in Task 2.5)
# SECRET_KEY=your-secret-key-here
# ACCESS_TOKEN_EXPIRE_MINUTES=30
\\\

---

##  Setup & Installation

### Prerequisites
- Python 3.12+
- Docker & Docker Compose
- Git

### Installation Steps

1. **Clone the repository**:
\\\ash
git clone <repository-url>
cd IDMS_WRFM
\\\

2. **Run setup script**:
\\\ash
chmod +x scripts/setup.sh
./scripts/setup.sh
\\\

Or manually:

3. **Start Docker services**:
\\\ash
docker-compose up -d
\\\

4. **Create virtual environment**:
\\\ash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\\\

5. **Install dependencies**:
\\\ash
cd backend
pip install -r requirements.txt
\\\

6. **Run database migrations**:
\\\ash
alembic upgrade head
\\\

7. **Start development server**:
\\\ash
python run.py
\\\

The API will be available at: http://localhost:8000

---

##  API Endpoints

### Health Checks 
- GET / - Root endpoint
- GET /health - Health check
- GET /api/v1/health - API health check

### Authentication  (Next - Task 2.5)
- POST /api/v1/auth/register - User registration
- POST /api/v1/auth/login - User login
- POST /api/v1/auth/refresh - Refresh token
- GET /api/v1/auth/me - Current user info

### Projects  (Task 2.6)
- GET /api/v1/projects - List projects
- POST /api/v1/projects - Create project
- GET /api/v1/projects/{id} - Get project
- PUT /api/v1/projects/{id} - Update project
- DELETE /api/v1/projects/{id} - Delete project

### RFIs  (Task 2.6)
- GET /api/v1/rfis - List RFIs
- POST /api/v1/rfis - Create RFI
- GET /api/v1/rfis/{id} - Get RFI
- PUT /api/v1/rfis/{id} - Update RFI
- DELETE /api/v1/rfis/{id} - Delete RFI

Interactive API documentation: http://localhost:8000/docs

---

##  Testing

*Tests will be implemented in Task 2.7*

\\\ash
cd backend
pytest
pytest --cov=app tests/
\\\

---

##  Database Migrations

### Create new migration:
\\\ash
cd backend
alembic revision --autogenerate -m "Description of changes"
\\\

### Apply migrations:
\\\ash
alembic upgrade head
\\\

### Rollback:
\\\ash
alembic downgrade -1
\\\

### View history:
\\\ash
alembic history
alembic current
\\\

---

##  Development Workflow

### Task Completion Protocol
Each task follows this workflow:
1.  Implement features
2.  Create/update database migrations (if needed)
3.  Update TODO.md (mark task complete)
4.  Update README.md (document changes)
5.  Update setup.sh (if needed)
6.  Git commit & push

---

##  Next Steps

### Immediate (Task 2.5)
- [ ] Implement authentication system
- [ ] Add JWT token generation
- [ ] Create auth endpoints
- [ ] Add password hashing

### Short-term (Phase 2)
- [ ] Complete CRUD operations (Task 2.6)
- [ ] Add pagination & filtering
- [ ] Write comprehensive tests (Task 2.7)
- [ ] Add API documentation

### Medium-term (Phase 3)
- [ ] Build Next.js frontend
- [ ] Create authentication UI
- [ ] Implement dashboard
- [ ] Build CRUD interfaces

---

##  Architecture Notes

### Design Patterns
- **Repository Pattern**: CRUD operations via CRUDBase
- **Dependency Injection**: FastAPI dependencies
- **Mixins**: Reusable model behaviors
- **Async/Await**: Full async support

### Best Practices
-  Type hints everywhere
-  Async database operations
-  Environment-based configuration
-  Database migrations version control
-  Soft delete for data retention
-  Automatic timestamps
-  Comprehensive logging

---

##  License

*To be determined*

---

##  Contributors

*Project in development*

---

##  Support

For issues or questions, please refer to the TODO.md file or create an issue in the repository.

---

**Last Updated**: 2025-10-31  
**Version**: 0.5.0 (Backend 50% complete)


###  User Management (Task 2.6)

**CRUD Operations:**
-  List users with pagination and filters
-  Get user by ID
-  Get current user profile
-  Create user (Admin only)
-  Update user (Self + Admin)
-  Soft delete user (Admin only)
-  Restore deleted user (Admin only)

**Features:**
- Advanced filtering (search, active status, superuser)
- Password validation (8+ chars, uppercase, lowercase, digit)
- Username uniqueness validation
- Email uniqueness validation
- Permission-based access control
- Self-profile management
- Soft delete mechanism

**Endpoints:**
\\\
GET    /api/v1/users/          - List users (Admin)
GET    /api/v1/users/me        - Current user
GET    /api/v1/users/{id}      - Get user
POST   /api/v1/users/          - Create user (Admin)
PUT    /api/v1/users/{id}      - Update user
DELETE /api/v1/users/{id}      - Soft delete (Admin)
POST   /api/v1/users/{id}/restore - Restore user (Admin)
\\\

**Security:**
- JWT authentication required
- Role-based access control (RBAC)
- Users can only view/edit their own profile
- Admins have full access
- Password hashing with bcrypt
