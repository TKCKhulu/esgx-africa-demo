"""
ESGx.Africa Organization Model
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON, Text, Float, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.db.session import Base

class OrganizationType(str, enum.Enum):
    """Organization types in African context"""
    PRIVATE_COMPANY = "private_company"
    PUBLIC_COMPANY = "public_company"
    SOE = "soe"  # State-Owned Enterprise
    NGO = "ngo"
    GOVERNMENT = "government"
    MINING = "mining"
    AGRICULTURE = "agriculture"
    FINANCIAL = "financial"
    MANUFACTURING = "manufacturing"
    SERVICES = "services"
    ENERGY = "energy"
    TELECOMMUNICATIONS = "telecommunications"

class BEELevel(str, enum.Enum):
    """Broad-Based Black Economic Empowerment levels"""
    LEVEL_1 = "level_1"
    LEVEL_2 = "level_2"
    LEVEL_3 = "level_3"
    LEVEL_4 = "level_4"
    LEVEL_5 = "level_5"
    LEVEL_6 = "level_6"
    LEVEL_7 = "level_7"
    LEVEL_8 = "level_8"
    NON_COMPLIANT = "non_compliant"

class Organization(Base):
    """Organization model for ESGx.Africa platform"""
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    registration_number = Column(String, unique=True)
    
    # Organization details
    organization_type = Column(SQLEnum(OrganizationType), nullable=False)
    industry_sector = Column(String, nullable=False)
    employee_count = Column(Integer)
    annual_revenue = Column(Float)  # in local currency
    
    # Location and African context
    country_code = Column(String, nullable=False)
    province_state = Column(String)
    city = Column(String)
    address = Column(Text)
    
    # African-specific compliance
    bee_level = Column(SQLEnum(BEELevel))
    bee_certificate_number = Column(String)
    bee_expiry_date = Column(DateTime)
    
    # ESG and sustainability
    sustainability_officer = Column(String)  # Contact person
    sustainability_email = Column(String)
    esg_policy_url = Column(String)
    carbon_neutral_target_year = Column(Integer)
    
    # Regulatory compliance
    jse_listed = Column(Boolean, default=False)
    regulatory_frameworks = Column(JSON)  # List of applicable frameworks
    compliance_status = Column(JSON)  # Current compliance status
    
    # Ubuntu philosophy integration
    ubuntu_initiatives = Column(JSON)  # Community-focused initiatives
    local_procurement_percentage = Column(Float)
    community_investment = Column(Float)  # Annual community investment
    
    # Subscription and platform usage
    subscription_plan = Column(String, default="community_free")
    white_label_enabled = Column(Boolean, default=False)
    api_access_enabled = Column(Boolean, default=False)
    
    # Contact information
    primary_contact_name = Column(String)
    primary_contact_email = Column(String)
    primary_contact_phone = Column(String)
    website = Column(String)
    
    # Platform settings
    preferred_language = Column(String, default="en")
    timezone = Column(String, default="Africa/Johannesburg")
    notification_preferences = Column(JSON)
    
    # Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    verification_documents = Column(JSON)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    users = relationship("User", backref="organization")
    esg_scores = relationship("ESGScore", back_populates="organization")
    esg_reports = relationship("ESGReport", back_populates="organization")
    carbon_data = relationship("CarbonData", back_populates="organization")
    compliance_records = relationship("ComplianceRecord", back_populates="organization")
    
    def __repr__(self):
        return f"<Organization(name='{self.name}', type='{self.organization_type}')>"
    
    @property
    def is_african_context(self) -> bool:
        """Check if organization is in African context"""
        african_countries = [
            "ZA", "KE", "NG", "GH", "UG", "TZ", "ZW", "BW", 
            "MW", "ZM", "MZ", "AO", "CI", "SN", "ML", "BF",
            "ET", "MA", "DZ", "TN", "EG", "LY", "SD", "SS"
        ]
        return self.country_code in african_countries
    
    @property
    def requires_bee_compliance(self) -> bool:
        """Check if organization requires BEE compliance (South Africa)"""
        return self.country_code == "ZA" and self.organization_type in [
            OrganizationType.PRIVATE_COMPANY,
            OrganizationType.PUBLIC_COMPANY,
            OrganizationType.SOE
        ]
    
    @property
    def ubuntu_score_weight(self) -> float:
        """Get Ubuntu philosophy weight in ESG scoring"""
        # Higher weight for organizations demonstrating Ubuntu values
        if self.ubuntu_initiatives and len(self.ubuntu_initiatives.get("initiatives", [])) > 0:
            return 0.3  # 30% weight for Ubuntu initiatives
        return 0.1  # Default 10% weight