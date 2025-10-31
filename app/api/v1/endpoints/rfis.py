"""
RFI API Endpoints
Task 2.7
"""
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, get_current_active_user, get_current_superuser
from app.crud import rfi as crud_rfi
from app.schemas.rfi import RFI, RFICreate, RFIUpdate, RFISearchFilters
from app.schemas.user import User

router = APIRouter()


@router.post("/", response_model=RFI, status_code=status.HTTP_201_CREATED)
def create_rfi(
    *,
    db: Session = Depends(get_db),
    rfi_in: RFICreate,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    ایجاد RFI جدید
    """
    # بررسی تکراری نبودن شماره RFI
    existing_rfi = crud_rfi.rfi.get_by_rfi_no(db, rfi_no=rfi_in.RFI_no)
    if existing_rfi:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"RFI with number {rfi_in.RFI_no} already exists"
        )
    
    rfi = crud_rfi.rfi.create(db, obj_in=rfi_in)
    return rfi


@router.get("/", response_model=List[RFI])
def read_rfis(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    دریافت لیست RFIها
    """
    rfis = crud_rfi.rfi.get_multi(db, skip=skip, limit=limit)
    return rfis


@router.get("/search", response_model=List[RFI])
def search_rfis(
    *,
    db: Session = Depends(get_db),
    rfi_no: str = Query(None),
    tag_no: str = Query(None),
    status: str = Query(None),
    step: str = Query(None),
    id_pre: int = Query(None),
    id_dis: int = Query(None),
    id_loc: int = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    جستجوی پیشرفته RFIها
    """
    filters = RFISearchFilters(
        RFI_no=rfi_no,
        tag_no=tag_no,
        status=status,
        step=step,
        id_pre=id_pre,
        id_dis=id_dis,
        id_loc=id_loc
    )
    
    rfis = crud_rfi.rfi.get_multi_with_filters(
        db, filters=filters, skip=skip, limit=limit
    )
    return rfis


@router.get("/pending", response_model=List[RFI])
def read_pending_rfis(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    دریافت RFIهای در انتظار بازرسی
    """
    rfis = crud_rfi.rfi.get_pending_inspections(db, skip=skip, limit=limit)
    return rfis


@router.get("/statistics")
def get_rfi_statistics(
    db: Session = Depends(get_db),
    project_id: int = Query(None),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    آمار RFIها
    """
    stats = crud_rfi.rfi.get_statistics(db, project_id=project_id)
    return stats


@router.get("/{id_rfi}", response_model=RFI)
def read_rfi(
    *,
    db: Session = Depends(get_db),
    id_rfi: int,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    دریافت اطلاعات یک RFI
    """
    rfi = crud_rfi.rfi.get(db, id=id_rfi)
    if not rfi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RFI not found"
        )
    return rfi


@router.put("/{id_rfi}", response_model=RFI)
def update_rfi(
    *,
    db: Session = Depends(get_db),
    id_rfi: int,
    rfi_in: RFIUpdate,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    به‌روزرسانی RFI
    """
    rfi = crud_rfi.rfi.get(db, id=id_rfi)
    if not rfi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RFI not found"
        )
    
    rfi = crud_rfi.rfi.update(db, db_obj=rfi, obj_in=rfi_in)
    return rfi


@router.post("/{id_rfi}/approve", response_model=RFI)
def approve_rfi(
    *,
    db: Session = Depends(get_db),
    id_rfi: int,
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    تایید RFI (نیاز به دسترسی بازرس)
    """
    rfi = crud_rfi.rfi.approve_rfi(
        db, id_rfi=id_rfi, inspector=current_user.full_name or current_user.username
    )
    if not rfi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RFI not found"
        )
    return rfi


@router.post("/{id_rfi}/reject", response_model=RFI)
def reject_rfi(
    *,
    db: Session = Depends(get_db),
    id_rfi: int,
    reason: str = Query(..., min_length=1),
    current_user: User = Depends(get_current_active_user)
) -> Any:
    """
    رد RFI (نیاز به دسترسی بازرس)
    """
    rfi = crud_rfi.rfi.reject_rfi(
        db,
        id_rfi=id_rfi,
        reason=reason,
        inspector=current_user.full_name or current_user.username
    )
    if not rfi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RFI not found"
        )
    return rfi


@router.post("/{id_rfi}/cancel", response_model=RFI)
def cancel_rfi(
    *,
    db: Session = Depends(get_db),
    id_rfi: int,
    reason: str = Query(..., min_length=1),
    current_user: User = Depends(get_current_superuser)
) -> Any:
    """
    کنسل کردن RFI (فقط برای Admin)
    """
    rfi = crud_rfi.rfi.cancel_rfi(db, id_rfi=id_rfi, reason=reason)
    if not rfi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RFI not found"
        )
    return rfi


@router.delete("/{id_rfi}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rfi(
    *,
    db: Session = Depends(get_db),
    id_rfi: int,
    current_user: User = Depends(get_current_superuser)
) -> None:
    """
    حذف RFI (فقط برای Admin)
    """
    rfi = crud_rfi.rfi.get(db, id=id_rfi)
    if not rfi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="RFI not found"
        )
    crud_rfi.rfi.remove(db, id=id_rfi)
