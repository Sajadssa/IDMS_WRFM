"""
CRUD operations for RFI
"""
from typing import List, Optional
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func

from app.models.rfi import GeneralRFI
from app.schemas.rfi import RFICreate, RFIUpdate


def create_rfi(db: Session, *, rfi_in: RFICreate) -> GeneralRFI:
    """ایجاد RFI جدید"""
    db_obj = GeneralRFI(**rfi_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_rfi(db: Session, *, rfi_id: int) -> Optional[GeneralRFI]:
    """دریافت RFI با ID"""
    return db.query(GeneralRFI).filter(GeneralRFI.id_RFI == rfi_id).first()


def get_rfi_by_no(db: Session, *, rfi_no: str) -> Optional[GeneralRFI]:
    """دریافت RFI با شماره"""
    return db.query(GeneralRFI).filter(GeneralRFI.RFI_no == rfi_no).first()


def get_rfis_by_tag(db: Session, *, tag_no: str) -> List[GeneralRFI]:
    """دریافت لیست RFI های یک تگ"""
    return db.query(GeneralRFI).filter(GeneralRFI.tag_no == tag_no).all()


def get_multi(
    db: Session, *, skip: int = 0, limit: int = 100
) -> List[GeneralRFI]:
    """دریافت لیست RFI ها"""
    return db.query(GeneralRFI).offset(skip).limit(limit).all()


def get_multi_with_filters(
    db: Session,
    *,
    skip: int = 0,
    limit: int = 100,
    rfi_no: Optional[str] = None,
    tag_no: Optional[str] = None,
    equipment_name: Optional[str] = None,
    status: Optional[str] = None,
    id_pre: Optional[int] = None,
    id_dis: Optional[int] = None,
    applicant: Optional[str] = None,
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
) -> List[GeneralRFI]:
    """جستجوی پیشرفته RFI"""
    query = db.query(GeneralRFI)
    
    if rfi_no:
        query = query.filter(GeneralRFI.RFI_no.ilike(f"%{rfi_no}%"))
    if tag_no:
        query = query.filter(GeneralRFI.tag_no.ilike(f"%{tag_no}%"))
    if equipment_name:
        query = query.filter(GeneralRFI.equipment_name.ilike(f"%{equipment_name}%"))
    if status:
        query = query.filter(GeneralRFI.status == status)
    if id_pre:
        query = query.filter(GeneralRFI.id_pre == id_pre)
    if id_dis:
        query = query.filter(GeneralRFI.id_dis == id_dis)
    if applicant:
        query = query.filter(GeneralRFI.Applicant.ilike(f"%{applicant}%"))
    if date_from:
        query = query.filter(GeneralRFI.RFI_date >= date_from)
    if date_to:
        query = query.filter(GeneralRFI.RFI_date <= date_to)
    
    return query.offset(skip).limit(limit).all()


def get_pending_inspections(
    db: Session, *, skip: int = 0, limit: int = 100
) -> List[GeneralRFI]:
    """دریافت RFI های در انتظار بازرسی"""
    return (
        db.query(GeneralRFI)
        .filter(
            and_(
                GeneralRFI.acc == False,
                GeneralRFI.rej == False,
                GeneralRFI.cancel == False
            )
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_rfi(
    db: Session, *, rfi_id: int, rfi_in: RFIUpdate
) -> Optional[GeneralRFI]:
    """به‌روزرسانی RFI"""
    db_obj = get_rfi(db, rfi_id=rfi_id)
    if not db_obj:
        return None
    
    update_data = rfi_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def approve_rfi(db: Session, *, rfi_id: int) -> Optional[GeneralRFI]:
    """تایید RFI"""
    db_obj = get_rfi(db, rfi_id=rfi_id)
    if not db_obj:
        return None
    
    db_obj.acc = True
    db_obj.rej = False
    db_obj.status = "Approved"
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def reject_rfi(
    db: Session, *, rfi_id: int, reason: str
) -> Optional[GeneralRFI]:
    """رد RFI"""
    db_obj = get_rfi(db, rfi_id=rfi_id)
    if not db_obj:
        return None
    
    db_obj.rej = True
    db_obj.acc = False
    db_obj.status = "Rejected"
    db_obj.note = f"Rejected: {reason}" + (f" | {db_obj.note}" if db_obj.note else "")
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def cancel_rfi(db: Session, *, rfi_id: int) -> Optional[GeneralRFI]:
    """کنسل کردن RFI"""
    db_obj = get_rfi(db, rfi_id=rfi_id)
    if not db_obj:
        return None
    
    db_obj.cancel = True
    db_obj.status = "Cancelled"
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def delete_rfi(db: Session, *, rfi_id: int) -> bool:
    """حذف RFI"""
    db_obj = get_rfi(db, rfi_id=rfi_id)
    if not db_obj:
        return False
    
    db.delete(db_obj)
    db.commit()
    return True


def get_statistics(db: Session) -> dict:
    """دریافت آمار RFI"""
    total = db.query(func.count(GeneralRFI.id_RFI)).scalar()
    approved = db.query(func.count(GeneralRFI.id_RFI)).filter(GeneralRFI.acc == True).scalar()
    rejected = db.query(func.count(GeneralRFI.id_RFI)).filter(GeneralRFI.rej == True).scalar()
    cancelled = db.query(func.count(GeneralRFI.id_RFI)).filter(GeneralRFI.cancel == True).scalar()
    pending = db.query(func.count(GeneralRFI.id_RFI)).filter(
        and_(
            GeneralRFI.acc == False,
            GeneralRFI.rej == False,
            GeneralRFI.cancel == False
        )
    ).scalar()
    
    return {
        "total": total,
        "approved": approved,
        "rejected": rejected,
        "cancelled": cancelled,
        "pending": pending
    }
