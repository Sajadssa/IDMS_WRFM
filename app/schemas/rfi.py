"""
RFI Schemas
"""
from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, validator


class RFIBase(BaseModel):
    """Base schema for RFI"""
    RFI_no: str = Field(..., min_length=1, max_length=50)
    RFI_date: date
    inspection_date: Optional[date] = None
    end_date: Optional[date] = None
    
    id_pre: Optional[int] = None
    id_dis: Optional[int] = None
    id_typ: Optional[int] = None
    id_loc: Optional[int] = None
    id_sys: Optional[int] = None
    id_sub: Optional[int] = None
    id_unit: Optional[int] = None
    id_area: Optional[int] = None
    id_com: Optional[int] = None
    
    Applicant: Optional[str] = Field(None, max_length=100)
    Performer: Optional[str] = Field(None, max_length=100)
    TPI: Optional[str] = Field(None, max_length=100)
    HeadQC: Optional[str] = Field(None, max_length=100)
    QC: Optional[str] = Field(None, max_length=100)
    inspctr: Optional[str] = Field(None, max_length=100)
    Contractor: Optional[str] = Field(None, max_length=100)
    
    status: Optional[str] = Field(None, max_length=50)
    step: Optional[str] = Field(None, max_length=50)
    
    tag_no: Optional[str] = Field(None, max_length=100)
    equipment_name: Optional[str] = Field(None, max_length=200)
    
    out_of_service: bool = False
    in_service: bool = False
    ready_to_service: bool = False
    
    note: Optional[str] = Field(None, max_length=500)
    attachment: Optional[str] = Field(None, max_length=200)

    @validator('inspection_date', 'end_date')
    def validate_dates(cls, v, values):
        if v and 'RFI_date' in values and v < values['RFI_date']:
            raise ValueError('تاریخ نمی‌تواند قبل از تاریخ RFI باشد')
        return v


class RFICreate(RFIBase):
    """Schema for creating RFI"""
    pass


class RFIUpdate(BaseModel):
    """Schema for updating RFI"""
    RFI_date: Optional[date] = None
    inspection_date: Optional[date] = None
    end_date: Optional[date] = None
    
    id_pre: Optional[int] = None
    id_dis: Optional[int] = None
    
    Applicant: Optional[str] = None
    Performer: Optional[str] = None
    
    status: Optional[str] = None
    step: Optional[str] = None
    
    tag_no: Optional[str] = None
    equipment_name: Optional[str] = None
    
    note: Optional[str] = None


class RFI(RFIBase):
    """Schema for RFI response"""
    id_RFI: int
    acc: bool
    rej: bool
    cancel: bool

    class Config:
        from_attributes = True


class RFISearchFilters(BaseModel):
    """Schema for RFI search filters"""
    RFI_no: Optional[str] = None
    tag_no: Optional[str] = None
    equipment_name: Optional[str] = None
    status: Optional[str] = None
    id_pre: Optional[int] = None
    id_dis: Optional[int] = None
    Applicant: Optional[str] = None
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    skip: int = 0
    limit: int = 100
