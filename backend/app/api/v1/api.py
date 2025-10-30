"""
API V1 Router
Includes all endpoint routers
"""
from fastapi import APIRouter

from app.api.v1.endpoints import health, auth, projects, rfis

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    projects.router,
    prefix="/projects",
    tags=["Projects"]
)

api_router.include_router(
    rfis.router,
    prefix="/rfis",
    tags=["RFIs"]
)
