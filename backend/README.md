# IDMS - Intelligent Document Management System

A comprehensive FastAPI-based project and document management system with advanced user management, authentication, and role-based access control.

##  Features

###  Completed Features

#### Authentication & Security
- **JWT Authentication**: Secure token-based authentication with access and refresh tokens
- **Password Security**: Bcrypt hashing with strong password validation
- **Role-Based Access Control (RBAC)**: Superuser and regular user roles
- **Token Management**: Token refresh and blacklist system
- **Session Management**: Login, logout, and password change endpoints

#### User Management
- **Complete CRUD Operations**: Create, read, update, and soft delete users
- **Advanced Filtering**: Search by username, email, active status, and role
- **Profile Management**: Users can view and update their own profiles
- **Password Validation**: Enforced strong passwords (min 8 chars, numbers, upper/lower case)
- **Soft Delete**: Safe user deletion with restore capability
- **User Listing**: Paginated user lists with filtering options

#### Database & Models
- **PostgreSQL Database**: Robust relational database
- **SQLAlchemy ORM**: Advanced object-relational mapping
- **Alembic Migrations**: Version-controlled database schema
- **Soft Delete Pattern**: Data preservation with deleted_at timestamps
- **Timestamp Tracking**: Automatic created_at and updated_at fields
- **Relationship Management**: Proper foreign keys and cascading

### 🔄 In Development
- Project Management CRUD
- Task Management System
- Document Management
- Activity Logging
- Real-time Notifications

##  Prerequisites

- Python 3.11+
- PostgreSQL 14+
- pip (Python package manager)

##  Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd idms

### 2. Create Virtual Environment
bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

### 3. Install Dependencies
bash
pip install -r requirements.txt

### 4. Configure Environment
Create a `.env` file in the project root:

env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/idms_db

# Security
SECRET_KEY=your-super-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Application
PROJECT_NAME=IDMS
VERSION=1.0.0
API_V1_STR=/api/v1

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

### 5. Initialize Database
bash
# Create database
createdb idms_db

# Run migrations
alembic upgrade head

# Create initial superuser
python scripts/create_superuser.py

##  Running the Application

### Development Server
bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### Access Points
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/api/v1/health

## 📚 API Documentation

### Authentication Endpoints

#### Login
bash
POST /api/v1/auth/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=Admin123!

**Response:**
json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}

#### Refresh Token
bash
POST /api/v1/auth/refresh
Authorization: Bearer <refresh_token>

#### Logout
bash
POST /api/v1/auth/logout
Authorization: Bearer <access_token>

### User Management Endpoints

#### List Users (Superuser only)
bash
GET /api/v1/users/?skip=0&limit=10&is_active=true
Authorization: Bearer <access_token>

**Query Parameters:**
- `skip`: Number of records to skip (pagination)
- `limit`: Maximum records to return
- `search`: Search in username/email
- `is_active`: Filter by active status
- `is_superuser`: Filter by superuser status

#### Get Current User
bash
GET /api/v1/users/me
Authorization: Bearer <access_token>

#### Get User by ID
bash
GET /api/v1/users/{user_id}
Authorization: Bearer <access_token>

#### Create User (Superuser only)
bash
POST /api/v1/users/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "SecurePass123",
  "full_name": "New User",
  "is_active": true,
  "is_superuser": false
}

#### Update User
bash
PUT /api/v1/users/{user_id}
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "full_name": "Updated Name",
  "email": "updated@example.com"
}

**Note:** Regular users can only update their own profile. Superusers can update any user.

#### Delete User (Soft Delete - Superuser only)
bash
DELETE /api/v1/users/{user_id}
Authorization: Bearer <access_token>

#### Restore User (Superuser only)
bash
POST /api/v1/users/{user_id}/restore
Authorization: Bearer <access_token>

##  Testing

### Run API Tests
bash
# Make sure server is running first
python tests/test_api.py

### Import Postman Collection
Import `tests/User_Management_API.postman_collection.json` into Postman for interactive testing.

### Test Credentials

Username: admin
Password: Admin123!
Role: Superuser

### Create Test Users
bash
python scripts/create_test_users.py

##  Project Structure


idms/
 app/
    api/
       dependencies.py      # Auth dependencies
       v1/
           api.py           # Main router
           endpoints/
               auth.py      # Authentication endpoints
               users.py     # User management endpoints
    core/
       config.py            # Configuration
       security.py          # Security utilities
    crud/
       user.py              # User CRUD operations
    db/
       base.py              # Database base
       session.py           # Database session
    models/
       user.py              # User model
       project.py           # Project model
       ...                  # Other models
    schemas/
       user.py              # User schemas
       token.py             # Token schemas
    main.py                  # FastAPI application
 alembic/
    versions/                # Database migrations
 scripts/
    create_superuser.py      # Superuser creation
    create_test_users.py     # Test data generator
 tests/
    test_api.py              # API tests
    *.postman_collection.json # Postman collections
 .env                         # Environment variables
 alembic.ini                  # Alembic configuration
 requirements.txt             # Python dependencies
 TODO.md                      # Development checklist
 README.md                    # This file

##  Security Features

### Password Security
- Minimum 8 characters
- Must contain uppercase and lowercase letters
- Must contain at least one number
- Bcrypt hashing with automatic salt generation

### Token Security
- JWT tokens with expiration
- Separate access and refresh tokens
- Token blacklist on logout
- Secure token validation

### Access Control
- Role-based permissions (RBAC)
- Superuser-only endpoints protected
- Users can only access their own data (unless superuser)
- Active user requirement for all operations

### Data Protection
- Soft delete pattern (data preservation)
- SQL injection protection via SQLAlchemy ORM
- CORS configuration
- Environment-based secrets

##  Development Roadmap

### Phase 2: Core Backend (60% Complete) 
- [x] Database Schema & Models
- [x] Authentication System
- [x] Core Utilities
- [x] Base Models & Mixins
- [x] User Management CRUD
- [ ] Project Management CRUD (In Progress)
- [ ] Task Management CRUD
- [ ] Comment System
- [ ] Document Management
- [ ] Activity Logging
- [ ] Advanced Features

### Phase 3: Testing (Not Started)
- [ ] Unit Tests
- [ ] Integration Tests
- [ ] API Tests
- [ ] Performance Tests

### Phase 4: Frontend (Not Started)
- [ ] React Application
- [ ] Authentication UI
- [ ] Dashboard
- [ ] Project Management UI
- [ ] Task Management UI

### Phase 5: Deployment (Not Started)
- [ ] Docker Configuration
- [ ] CI/CD Pipeline
- [ ] Production Setup
- [ ] Monitoring

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Contact

For questions or support, please open an issue on GitHub.

---

**Current Version:** 1.0.0  
**Last Updated:** 2025-10-31  
**Status:** Active Development (Phase 2 - 60% Complete)
