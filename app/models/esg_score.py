"""
ESGx.Africa ESG Score Model with Ubuntu Index
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from app.db.session import Base

class ESGScore(Base):
    """ESG Score model with Ubuntu Index for African context"""
    __tablename__ = "esg_scores"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    
    # Core ESG Scores (0-100 scale)
    environmental_score = Column(Float, nullable=False)
    social_score = Column(Float, nullable=False)
    governance_score = Column(Float, nullable=False)
    overall_esg_score = Column(Float, nullable=False)
    
    # Ubuntu Index™ - African philosophy integration
    ubuntu_index = Column(Float, nullable=False)  # Ubuntu philosophy score
    community_engagement_score = Column(Float, default=0.0)
    local_procurement_score = Column(Float, default=0.0)
    cultural_preservation_score = Column(Float, default=0.0)
    indigenous_knowledge_score = Column(Float, default=0.0)
    
    # African-specific metrics
    bee_compliance_score = Column(Float, default=0.0)  # BEE compliance
    local_employment_score = Column(Float, default=0.0)
    community_investment_score = Column(Float, default=0.0)
    land_rights_score = Column(Float, default=0.0)
    
    # Detailed component scores
    environmental_components = Column(JSON)  # Detailed breakdown
    social_components = Column(JSON)
    governance_components = Column(JSON)
    ubuntu_components = Column(JSON)
    
    # Framework-specific scores
    gri_score = Column(Float)
    sasb_score = Column(Float)
    tcfd_score = Column(Float)
    sdg_alignment_score = Column(Float)
    
    # Risk assessments
    environmental_risk_level = Column(String)  # low, medium, high, critical
    social_risk_level = Column(String)
    governance_risk_level = Column(String)
    overall_risk_level = Column(String)
    
    # Data quality and confidence
    data_quality_score = Column(Float, default=0.0)  # 0-100
    confidence_level = Column(Float, default=0.0)  # 0-100
    data_sources = Column(JSON)  # List of data sources used
    
    # Temporal information
    reporting_period_start = Column(DateTime, nullable=False)
    reporting_period_end = Column(DateTime, nullable=False)
    calculation_date = Column(DateTime, server_default=func.now())
    
    # AI-generated insights
    ai_insights = Column(JSON)  # AI-generated recommendations
    improvement_areas = Column(JSON)  # Areas for improvement
    benchmarks = Column(JSON)  # Industry/regional benchmarks
    
    # Verification and audit
    is_verified = Column(Boolean, default=False)
    verification_date = Column(DateTime)
    verification_body = Column(String)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="esg_scores")
    organization = relationship("Organization", back_populates="esg_scores")
    
    def __repr__(self):
        return f"<ESGScore(org_id={self.organization_id}, overall={self.overall_esg_score}, ubuntu={self.ubuntu_index})>"
    
    @property
    def esg_rating(self) -> str:
        """Get ESG rating based on overall score"""
        if self.overall_esg_score >= 90:
            return "AAA"
        elif self.overall_esg_score >= 80:
            return "AA"
        elif self.overall_esg_score >= 70:
            return "A"
        elif self.overall_esg_score >= 60:
            return "BBB"
        elif self.overall_esg_score >= 50:
            return "BB"
        elif self.overall_esg_score >= 40:
            return "B"
        elif self.overall_esg_score >= 30:
            return "CCC"
        elif self.overall_esg_score >= 20:
            return "CC"
        else:
            return "C"
    
    @property
    def ubuntu_rating(self) -> str:
        """Get Ubuntu philosophy rating"""
        if self.ubuntu_index >= 85:
            return "Ubuntu Champion"
        elif self.ubuntu_index >= 70:
            return "Ubuntu Advocate"
        elif self.ubuntu_index >= 55:
            return "Ubuntu Aligned"
        elif self.ubuntu_index >= 40:
            return "Ubuntu Developing"
        else:
            return "Ubuntu Opportunity"
    
    def calculate_weighted_score(self, weights: dict = None) -> float:
        """Calculate weighted ESG score with Ubuntu integration"""
        if weights is None:
            # Default African-contextualized weights
            weights = {
                "environmental": 0.25,
                "social": 0.35,  # Higher weight on social in African context
                "governance": 0.25,
                "ubuntu": 0.15   # Ubuntu philosophy integration
            }
        
        weighted_score = (
            self.environmental_score * weights["environmental"] +
            self.social_score * weights["social"] +
            self.governance_score * weights["governance"] +
            self.ubuntu_index * weights["ubuntu"]
        )
        
        return round(weighted_score, 2)
    
    @property
    def is_above_benchmark(self) -> bool:
        """Check if score is above regional benchmark"""
        # African ESG benchmark average (can be configurable)
        african_benchmark = 55.0
        return self.overall_esg_score > african_benchmark