from sqlalchemy import Column, String, Text, Integer, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from enum import Enum
from backend.app.models.base import BaseModel


class ProjectStatus(str, Enum):
    """Project status enumeration"""
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Project(BaseModel):
    """Project model for construction projects"""
    __tablename__ = "projects"

    name = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    project_code = Column(String(50), unique=True, nullable=False, index=True)
    status = Column(SQLEnum(ProjectStatus), default=ProjectStatus.PLANNING, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # Relationships
    owner = relationship("User", back_populates="projects")
    rfis = relationship("RFI", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}', code='{self.project_code}')>"
