"""
Test data creation script for User Management
Run after creating first superuser
"""
import sys
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.crud.user import user as user_crud
from app.schemas.user import UserCreate


def create_test_users():
    """Create test users for development"""
    db: Session = SessionLocal()
    
    try:
        # Test users data
        test_users = [
            {
                "username": "john_doe",
                "email": "john@example.com",
                "password": "TestPass123",
                "full_name": "John Doe",
                "is_active": True,
                "is_superuser": False
            },
            {
                "username": "jane_smith",
                "email": "jane@example.com",
                "password": "TestPass123",
                "full_name": "Jane Smith",
                "is_active": True,
                "is_superuser": False
            },
            {
                "username": "bob_wilson",
                "email": "bob@example.com",
                "password": "TestPass123",
                "full_name": "Bob Wilson",
                "is_active": False,  # Inactive user for testing
                "is_superuser": False
            }
        ]
        
        created = 0
        skipped = 0
        
        for user_data in test_users:
            # Check if user exists
            existing = user_crud.get_by_username(db, username=user_data["username"])
            if existing:
                print(f"  User {user_data['username']} already exists, skipping...")
                skipped += 1
                continue
            
            # Create user
            user_in = UserCreate(**user_data)
            user = user_crud.create(db, obj_in=user_in)
            print(f" Created user: {user.username} ({user.email})")
            created += 1
        
        print(f"\n Summary: {created} created, {skipped} skipped")
        
    except Exception as e:
        print(f" Error: {str(e)}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print(" Creating test users...\n")
    create_test_users()
    print("\n Done!")
