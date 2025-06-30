"""
ESGx.Africa Database Base Configuration
Import all models here for proper table creation
"""

from app.db.session import Base

# Import all models here so they are registered with SQLAlchemy
from app.models.user import User
from app.models.organization import Organization
from app.models.esg_score import ESGScore
from app.models.esg_report import ESGReport
from app.models.carbon_data import CarbonData
from app.models.compliance import ComplianceRecord
from app.models.ai_agent import AIAgent, AIConversation