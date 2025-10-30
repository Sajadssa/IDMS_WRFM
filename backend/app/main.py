from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="RFI Management System",
    description="Request for Information Management API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "RFI Management API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
"""
Main FastAPI Application
RFI Management System
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.api.v1.api import api_router
from app.middleware.logging_middleware import LoggingMiddleware

# Create FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="RFI Management System API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host Middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS
)

# Custom Logging Middleware
app.add_middleware(LoggingMiddleware)

# Include API Router
app.include_router(api_router, prefix="/api/v1")


# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "RFI Management System API",
        "version": settings.VERSION,
        "docs": "/api/docs"
    }


# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }


# Startup event
@app.on_event("startup")
async def startup_event():
    """Startup tasks"""
    print(f"🚀 Starting {settings.PROJECT_NAME} v{settings.VERSION}")
    print(f"📝 Environment: {settings.ENVIRONMENT}")
    print(f"📚 API Docs: http://localhost:8000/api/docs")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown tasks"""
    print(f"👋 Shutting down {settings.PROJECT_NAME}")
