from sqlalchemy import Column, String, Text, Integer, ForeignKey, Date, Enum as SQLEnum
from sqlalchemy.orm import relationship
from enum import Enum
from backend.app.models.base import BaseModel


class RFIStatus(str, Enum):
    """RFI status enumeration"""
    DRAFT = "draft"
    SUBMITTED = "submitted"
    IN_REVIEW = "in_review"
    ANSWERED = "answered"
    CLOSED = "closed"
    CANCELLED = "cancelled"


class RFIPriority(str, Enum):
    """RFI priority enumeration"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class RFI(BaseModel):
    """RFI (Request for Information) model"""
    __tablename__ = "rfis"

    rfi_number = Column(String(50), unique=True, nullable=False, index=True)
    subject = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(SQLEnum(RFIStatus), default=RFIStatus.DRAFT, nullable=False)
    priority = Column(SQLEnum(RFIPriority), default=RFIPriority.MEDIUM, nullable=False)
    
    due_date = Column(Date, nullable=True)
    response = Column(Text, nullable=True)
    
    # Foreign Keys
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    creator_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    project = relationship("Project", back_populates="rfis")
    creator = relationship("User", back_populates="rfis")

    def __repr__(self):
        return f"<RFI(id={self.id}, number='{self.rfi_number}', subject='{self.subject}')>"
