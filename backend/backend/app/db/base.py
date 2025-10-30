from datetime import datetime
from typing import Any
from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    Provides common functionality and configurations.
    """
    pass


class TimestampMixin:
    """
    Mixin for automatic timestamp management.
    Adds created_at and updated_at fields to models.
    """
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="Timestamp when record was created"
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="Timestamp when record was last updated"
    )


class SoftDeleteMixin:
    """
    Mixin for soft delete functionality.
    Instead of deleting records, marks them as deleted.
    """
    
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        comment="Timestamp when record was soft deleted"
    )
    
    @property
    def is_deleted(self) -> bool:
        """Check if record is soft deleted"""
        return self.deleted_at is not None
    
    def soft_delete(self) -> None:
        """Mark record as deleted"""
        self.deleted_at = datetime.utcnow()
    
    def restore(self) -> None:
        """Restore soft deleted record"""
        self.deleted_at = None


class UserTrackingMixin:
    """
    Mixin for tracking user who created/modified records.
    Requires foreign key to User model.
    """
    
    @declared_attr
    def created_by_id(cls) -> Mapped[int | None]:
        from sqlalchemy import ForeignKey
        return mapped_column(
            ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
            comment="User who created this record"
        )
    
    @declared_attr
    def updated_by_id(cls) -> Mapped[int | None]:
        from sqlalchemy import ForeignKey
        return mapped_column(
            ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
            comment="User who last updated this record"
        )


class BaseModel(Base, TimestampMixin):
    """
    Base model that includes timestamp functionality.
    All application models should inherit from this.
    """
    
    __abstract__ = True
    
    def to_dict(self) -> dict[str, Any]:
        """
        Convert model instance to dictionary.
        Useful for serialization and debugging.
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }
    
    def __repr__(self) -> str:
        """String representation of model"""
        attrs = ", ".join(
            f"{k}={v!r}"
            for k, v in self.to_dict().items()
            if not k.startswith("_")
        )
        return f"{self.__class__.__name__}({attrs})"
