"""
Application Configuration
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # Project Info
    PROJECT_NAME: str = "RFI Management System"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://rfi_user:rfi_password@localhost:5432/rfi_db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]
    
    # Trusted Hosts
    ALLOWED_HOSTS: List[str] = [
        "localhost",
        "127.0.0.1",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
