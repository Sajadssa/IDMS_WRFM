"""
User management endpoints
"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.user import user as user_crud
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UserListResponse
)
from app.models.user import User
from app.api.dependencies import (
    get_current_active_user,
    get_current_superuser
)

router = APIRouter()


# ============================================
# List Users (with filters)
# ============================================
@router.get("/", response_model=UserListResponse)
def list_users(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    search: Optional[str] = Query(None, description="Search in username, email, or full_name"),
    is_active: Optional[bool] = Query(None, description="Filter by active status"),
    is_superuser: Optional[bool] = Query(None, description="Filter by superuser status"),
    current_user: User = Depends(get_current_superuser)
):
    """
    Get list of users with filters (Admin only)
    
    - **skip**: Number of records to skip (pagination)
    - **limit**: Maximum number of records to return
    - **search**: Search term for username, email, or full_name
    - **is_active**: Filter by active status
    - **is_superuser**: Filter by superuser status
    """
    users = user_crud.get_multi_with_filters(
        db,
        skip=skip,
        limit=limit,
        search=search,
        is_active=is_active,
        is_superuser=is_superuser
    )
    
    # Get total count (same filters without pagination)
    total_query = db.query(User)
    if search:
        from sqlalchemy import or_
        total_query = total_query.filter(
            or_(
                User.username.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                User.full_name.ilike(f"%{search}%")
            )
        )
    if is_active is not None:
        total_query = total_query.filter(User.is_active == is_active)
    if is_superuser is not None:
        total_query = total_query.filter(User.is_superuser == is_superuser)
    
    total = total_query.count()
    
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "users": users
    }


# ============================================
# Get Current User
# ============================================
@router.get("/me", response_model=UserResponse)
def get_current_user_info(
    current_user: User = Depends(get_current_active_user)
):
    """
    Get current logged-in user information
    """
    return current_user


# ============================================
# Get User by ID
# ============================================
@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Get user by ID
    
    - Regular users can only view their own profile
    - Admins can view any user
    """
    # Check permissions
    if user_id != current_user.id and not user_crud.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user


# ============================================
# Create User (Admin only)
# ============================================
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """
    Create new user (Admin only)
    
    Password requirements:
    - At least 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    """
    # Check if username exists
    if user_crud.get_by_username(db, username=user_in.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email exists
    if user_crud.get_by_email(db, email=user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user = user_crud.create(db, obj_in=user_in)
    return user


# ============================================
# Update User
# ============================================
@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Update user
    
    - Regular users can only update their own profile (except is_superuser)
    - Admins can update any user
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check permissions
    if user_id != current_user.id and not user_crud.is_superuser(current_user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    # Regular users cannot change superuser status
    if not user_crud.is_superuser(current_user) and user_in.is_superuser is not None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot change superuser status"
        )
    
    # Check username uniqueness if changed
    if user_in.username and user_in.username != user.username:
        if user_crud.get_by_username(db, username=user_in.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
    
    # Check email uniqueness if changed
    if user_in.email and user_in.email != user.email:
        if user_crud.get_by_email(db, email=user_in.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    user = user_crud.update(db, db_obj=user, obj_in=user_in)
    return user


# ============================================
# Delete User (Soft Delete)
# ============================================
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """
    Soft delete user (Admin only)
    
    This marks the user as inactive but doesn't remove from database
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Prevent deleting yourself
    if user_id == current_user.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete yourself"
        )
    
    # Soft delete by setting is_active to False
    user_crud.update(db, db_obj=user, obj_in={"is_active": False})
    return None


# ============================================
# Restore User
# ============================================
@router.post("/{user_id}/restore", response_model=UserResponse)
def restore_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_superuser)
):
    """
    Restore soft-deleted user (Admin only)
    
    This reactivates an inactive user
    """
    user = user_crud.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already active"
        )
    
    user = user_crud.update(db, db_obj=user, obj_in={"is_active": True})
    return user
