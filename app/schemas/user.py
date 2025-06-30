"""
ESGx.Africa User Schemas
"""

from typing import Optional, Dict, List, Any
from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.models.user import SubscriptionPlan, UserRole

class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    full_name: str
    country_code: str
    preferred_language: Optional[str] = "en"
    phone_number: Optional[str] = None
    job_title: Optional[str] = None

class UserUpdate(BaseModel):
    """User update schema"""
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    job_title: Optional[str] = None
    preferred_language: Optional[str] = None
    ubuntu_profile: Optional[Dict[str, Any]] = None
    esg_frameworks: Optional[List[str]] = None
    notification_preferences: Optional[Dict[str, Any]] = None

class UserSubscriptionUpdate(BaseModel):
    """Update user subscription"""
    subscription_plan: SubscriptionPlan

class UserProfile(UserBase):
    """Extended user profile"""
    id: int
    subscription_plan: SubscriptionPlan
    role: UserRole
    is_active: bool
    is_verified: bool
    ubuntu_profile: Optional[Dict[str, Any]] = None
    organization_id: Optional[int] = None
    reports_used_this_month: int
    ai_queries_used_this_month: int
    max_reports_per_month: int
    max_ai_agents: int
    can_use_ai_agents: bool
    esg_frameworks: Optional[List[str]] = None
    notification_preferences: Optional[Dict[str, Any]] = None
    last_login: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserUsageStats(BaseModel):
    """User usage statistics"""
    reports_generated: int
    ai_conversations: int
    carbon_assessments: int
    compliance_checks: int
    current_month_usage: Dict[str, int]
    subscription_limits: Dict[str, Any]
    usage_percentage: Dict[str, float]