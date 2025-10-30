"""
API v1 router configuration
"""
from fastapi import APIRouter
from backend.app.api.v1.endpoints import health, auth, projects, rfis

router = APIRouter()

# Include all endpoint routers
router.include_router(health.router, prefix="/health", tags=["Health"])
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(projects.router, prefix="/projects", tags=["Projects"])
router.include_router(rfis.router, prefix="/rfis", tags=["RFIs"])
