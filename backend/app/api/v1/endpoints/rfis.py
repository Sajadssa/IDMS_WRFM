"""
RFIs Endpoints (Placeholder)
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_rfis():
    """List RFIs (placeholder)"""
    return {"message": "List RFIs - to be implemented"}


@router.post("/")
async def create_rfi():
    """Create RFI (placeholder)"""
    return {"message": "Create RFI - to be implemented"}


@router.get("/{rfi_id}")
async def get_rfi(rfi_id: int):
    """Get RFI (placeholder)"""
    return {"message": f"Get RFI {rfi_id} - to be implemented"}
