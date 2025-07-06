"""
ESGx.Africa Authentication Schemas
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.models.user import SubscriptionPlan

class UserLogin(BaseModel):
    """User login request"""
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    """User registration request"""
    email: EmailStr
    password: str
    full_name: str
    country_code: str
    preferred_language: Optional[str] = "en"
    phone_number: Optional[str] = None
    job_title: Optional[str] = None
    subscription_plan: Optional[SubscriptionPlan] = SubscriptionPlan.COMMUNITY_FREE

class UserResponse(BaseModel):
    """User response model"""
    id: int
    email: EmailStr
    full_name: str
    country_code: str
    preferred_language: str
    subscription_plan: SubscriptionPlan
    is_active: bool
    is_verified: bool
    phone_number: Optional[str] = None
    job_title: Optional[str] = None
    organization_id: Optional[int] = None
    reports_used_this_month: Optional[int] = None
    ai_queries_used_this_month: Optional[int] = None
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    """Access token response"""
    access_token: str
    token_type: str
    expires_in: int
    user: Optional[Dict[str, Any]] = None

class TokenData(BaseModel):
    """Token data for validation"""
    username: Optional[str] = None