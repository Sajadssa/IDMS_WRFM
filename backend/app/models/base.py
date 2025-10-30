from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr
from backend.app.database import Base


class BaseModel(Base):
    """Base model class with common fields for all models"""
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    @declared_attr
    def __tablename__(cls) -> str:
        """Auto-generate table name from class name"""
        return cls.__name__.lower() + 's'

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
