"""
RFI (Request For Inspection) Model
مدل درخواست بازرسی
"""
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class GeneralRFI(Base):
    """مدل اصلی RFI"""
    __tablename__ = "Tbl_RFI"
    __table_args__ = {"schema": "QC"}

    # Primary Key
    id_RFI = Column(Integer, primary_key=True, index=True)

    # RFI Information
    RFI_no = Column(String(50), unique=True, index=True, nullable=False)
    RFI_date = Column(Date, nullable=False)
    inspection_date = Column(Date)
    end_date = Column(Date)

    # Foreign Keys (Integer type as per original table)
    id_pre = Column(Integer, ForeignKey("dbo.Tbl_Project.id_pre"))
    id_dis = Column(Integer, ForeignKey("dbo.Tbl_Discipline.id_dis"))
    id_typ = Column(Integer, ForeignKey("QC.Tbl_Type.id_typ"))
    id_loc = Column(Integer, ForeignKey("dbo.Tbl_Location.id_loc"))
    id_sys = Column(Integer, ForeignKey("dbo.Tbl_Systems.id_sys"))
    id_sub = Column(Integer, ForeignKey("dbo.Tbl_Subsystem.id_sub"))
    id_unit = Column(Integer, ForeignKey("dbo.Tbl_Unit.id_unit"))
    id_area = Column(Integer, ForeignKey("dbo.Tbl_Area.id_area"))
    id_com = Column(Integer, ForeignKey("dbo.Tbl_Contractor.id_com"))

    # Inspectors and Personnel
    Applicant = Column(String(100))
    Performer = Column(String(100))
    TPI = Column(String(100))
    HeadQC = Column(String(100))
    QC = Column(String(100))
    inspctr = Column(String(100))
    Contractor = Column(String(100))

    # Status Fields
    acc = Column(Boolean, default=False)
    rej = Column(Boolean, default=False)
    status = Column(String(50))
    step = Column(String(50))
    cancel = Column(Boolean, default=False)

    # Equipment Information
    tag_no = Column(String(100), index=True)
    equipment_name = Column(String(200))

    # Service Status
    out_of_service = Column(Boolean, default=False)
    in_service = Column(Boolean, default=False)
    ready_to_service = Column(Boolean, default=False)

    # Additional Fields
    note = Column(String(500))
    attachment = Column(String(200))

    # Relationships
    project = relationship("Project", foreign_keys=[id_pre], backref="rfis")

    def __repr__(self):
        return f"<GeneralRFI(id={self.id_RFI}, RFI_no='{self.RFI_no}', status='{self.status}')>"


# Create indexes
Index('idx_rfi_no', GeneralRFI.RFI_no)
Index('idx_rfi_tag', GeneralRFI.tag_no)
Index('idx_rfi_date', GeneralRFI.RFI_date)
Index('idx_rfi_status', GeneralRFI.status)
