"""
ESGx.Africa User Model
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.db.session import Base

class UserRole(str, enum.Enum):
    """User role types"""
    ADMIN = "admin"
    ESG_MANAGER = "esg_manager"
    COMPLIANCE_OFFICER = "compliance_officer"
    ANALYST = "analyst"
    USER = "user"

class SubscriptionPlan(str, enum.Enum):
    """Subscription plan types"""
    COMMUNITY_FREE = "community_free"
    UBUNTU_STARTER = "ubuntu_starter"
    GROWTH_PRO = "growth_pro"
    ENTERPRISE_ESG = "enterprise_esg"
    ENTERPRISE_PLUS = "enterprise_plus"

class User(Base):
    """User model for ESGx.Africa platform"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    
    # African/Ubuntu context
    preferred_language = Column(String, default="en")  # ISO language code
    country_code = Column(String, nullable=False)  # African country
    ubuntu_profile = Column(JSON)  # Ubuntu philosophy alignment data
    
    # Subscription and access
    subscription_plan = Column(
        SQLEnum(SubscriptionPlan), 
        default=SubscriptionPlan.COMMUNITY_FREE
    )
    role = Column(SQLEnum(UserRole), default=UserRole.USER)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    
    # Usage tracking
    reports_used_this_month = Column(Integer, default=0)
    ai_queries_used_this_month = Column(Integer, default=0)
    last_login = Column(DateTime)
    
    # Profile information
    phone_number = Column(String)
    organization_id = Column(Integer, nullable=True)  # Link to organization
    job_title = Column(String)
    
    # ESG-specific preferences
    esg_frameworks = Column(JSON)  # Preferred ESG frameworks
    notification_preferences = Column(JSON)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    esg_scores = relationship("ESGScore", back_populates="user")
    esg_reports = relationship("ESGReport", back_populates="user")
    ai_conversations = relationship("AIConversation", back_populates="user")
    
    def __repr__(self):
        return f"<User(email='{self.email}', plan='{self.subscription_plan}')>"
    
    @property
    def can_use_ai_agents(self) -> bool:
        """Check if user can access AI agents based on subscription"""
        ai_agent_plans = [
            SubscriptionPlan.UBUNTU_STARTER,
            SubscriptionPlan.GROWTH_PRO,
            SubscriptionPlan.ENTERPRISE_ESG,
            SubscriptionPlan.ENTERPRISE_PLUS
        ]
        return self.subscription_plan in ai_agent_plans
    
    @property
    def max_reports_per_month(self) -> int:
        """Get max reports allowed per month based on subscription"""
        limits = {
            SubscriptionPlan.COMMUNITY_FREE: 3,
            SubscriptionPlan.UBUNTU_STARTER: 50,
            SubscriptionPlan.GROWTH_PRO: 500,
            SubscriptionPlan.ENTERPRISE_ESG: -1,  # unlimited
            SubscriptionPlan.ENTERPRISE_PLUS: -1  # unlimited
        }
        return limits.get(self.subscription_plan, 3)
    
    @property
    def max_ai_agents(self) -> int:
        """Get max AI agents allowed based on subscription"""
        limits = {
            SubscriptionPlan.COMMUNITY_FREE: 0,
            SubscriptionPlan.UBUNTU_STARTER: 1,
            SubscriptionPlan.GROWTH_PRO: 2,
            SubscriptionPlan.ENTERPRISE_ESG: 5,
            SubscriptionPlan.ENTERPRISE_PLUS: -1  # unlimited
        }
        return limits.get(self.subscription_plan, 0)