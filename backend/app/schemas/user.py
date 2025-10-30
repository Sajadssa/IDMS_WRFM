"""
User Pydantic schemas for request/response validation
"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, validator


# ============================================
# Base Schema
# ============================================
class UserBase(BaseModel):
    """Base user schema with common fields"""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


# ============================================
# Create Schema
# ============================================
class UserCreate(UserBase):
    """Schema for creating a new user"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)
    
    @validator('password')
    def validate_password(cls, v):
        """Validate password strength"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        return v
    
    @validator('username')
    def validate_username(cls, v):
        """Validate username format"""
        if not v.isalnum() and '_' not in v:
            raise ValueError('Username can only contain letters, numbers and underscores')
        return v


# ============================================
# Update Schema
# ============================================
class UserUpdate(UserBase):
    """Schema for updating a user"""
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    
    @validator('password')
    def validate_password(cls, v):
        """Validate password strength if provided"""
        if v is None:
            return v
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError('Password must contain at least one lowercase letter')
        return v


# ============================================
# Response Schemas
# ============================================
class UserInDB(UserBase):
    """Schema for user as stored in database"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserResponse(UserInDB):
    """Schema for user in API responses"""
    pass


class UserListResponse(BaseModel):
    """Schema for paginated user list"""
    total: int
    skip: int
    limit: int
    users: list[UserResponse]
