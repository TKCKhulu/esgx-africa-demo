"""
ESGx.Africa ESG Report Model
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey, Boolean, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.db.session import Base

class ReportType(str, enum.Enum):
    """Types of ESG reports"""
    ANNUAL_SUSTAINABILITY = "annual_sustainability"
    QUARTERLY_UPDATE = "quarterly_update"
    REGULATORY_COMPLIANCE = "regulatory_compliance"
    STAKEHOLDER_REPORT = "stakeholder_report"
    INVESTOR_PRESENTATION = "investor_presentation"
    COMMUNITY_IMPACT = "community_impact"
    BEE_COMPLIANCE = "bee_compliance"
    JSE_SUSTAINABILITY = "jse_sustainability"
    CUSTOM = "custom"

class ReportStatus(str, enum.Enum):
    """Report generation and approval status"""
    DRAFT = "draft"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    PUBLISHED = "published"
    ARCHIVED = "archived"

class ESGReport(Base):
    """ESG Report model for comprehensive sustainability reporting"""
    __tablename__ = "esg_reports"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Report creator
    esg_score_id = Column(Integer, ForeignKey("esg_scores.id"), nullable=True)
    
    # Report metadata
    title = Column(String, nullable=False)
    report_type = Column(SQLEnum(ReportType), nullable=False)
    status = Column(SQLEnum(ReportStatus), default=ReportStatus.DRAFT)
    version = Column(String, default="1.0")
    
    # Reporting period
    reporting_period_start = Column(DateTime, nullable=False)
    reporting_period_end = Column(DateTime, nullable=False)
    reporting_year = Column(Integer, nullable=False)
    
    # Frameworks and standards
    frameworks_used = Column(JSON, nullable=False)  # GRI, SASB, TCFD, etc.
    african_standards_compliance = Column(JSON)  # BEE, JSE, local regulations
    international_alignment = Column(JSON)  # UN SDGs, Paris Agreement, etc.
    
    # Report structure and content
    executive_summary = Column(Text)
    environmental_section = Column(JSON)
    social_section = Column(JSON)
    governance_section = Column(JSON)
    ubuntu_section = Column(JSON)  # Ubuntu philosophy integration
    
    # African-specific sections
    community_impact_section = Column(JSON)
    bee_compliance_section = Column(JSON)
    local_procurement_section = Column(JSON)
    cultural_preservation_section = Column(JSON)
    
    # Performance data
    key_metrics = Column(JSON)  # Key performance indicators
    targets_and_commitments = Column(JSON)
    progress_against_targets = Column(JSON)
    materiality_assessment = Column(JSON)
    
    # Stakeholder engagement
    stakeholder_feedback = Column(JSON)
    community_consultation_results = Column(JSON)
    employee_engagement_data = Column(JSON)
    investor_concerns_addressed = Column(JSON)
    
    # Risk and opportunity analysis
    esg_risks_identified = Column(JSON)
    climate_risks = Column(JSON)
    social_risks = Column(JSON)
    governance_risks = Column(JSON)
    opportunities = Column(JSON)
    
    # Third-party verification
    is_verified = Column(Boolean, default=False)
    verification_body = Column(String)
    verification_level = Column(String)  # limited, reasonable, etc.
    verification_date = Column(DateTime)
    verification_opinion = Column(Text)
    
    # AI-generated content
    ai_insights = Column(JSON)  # AI-generated insights
    ai_recommendations = Column(JSON)
    auto_generated_sections = Column(JSON)  # Which sections were AI-generated
    
    # Multi-language support
    primary_language = Column(String, default="en")
    available_languages = Column(JSON)  # List of available translations
    translation_status = Column(JSON)  # Translation completion status
    
    # Document generation
    pdf_generated = Column(Boolean, default=False)
    pdf_file_path = Column(String)
    word_doc_generated = Column(Boolean, default=False)
    word_doc_file_path = Column(String)
    html_version_url = Column(String)
    
    # Distribution and sharing
    published_url = Column(String)
    shared_with_stakeholders = Column(JSON)  # List of stakeholders shared with
    public_access_enabled = Column(Boolean, default=False)
    download_count = Column(Integer, default=0)
    
    # Approval workflow
    approved_by = Column(String)  # User ID who approved
    approval_date = Column(DateTime)
    approval_comments = Column(Text)
    review_cycle_days = Column(Integer)
    
    # Compliance and regulatory
    regulatory_submissions = Column(JSON)  # Where/when submitted to regulators
    compliance_certificates = Column(JSON)  # Associated compliance certificates
    regulatory_feedback = Column(JSON)  # Feedback from regulatory bodies
    
    # Performance benchmarking
    industry_benchmark_comparison = Column(JSON)
    peer_company_comparison = Column(JSON)
    regional_benchmark_comparison = Column(JSON)
    year_over_year_comparison = Column(JSON)
    
    # Ubuntu philosophy integration
    ubuntu_philosophy_score = Column(Float)
    community_benefit_quantified = Column(JSON)
    local_economic_impact = Column(JSON)
    cultural_sensitivity_assessment = Column(JSON)
    
    # Digital features
    interactive_dashboard_url = Column(String)
    data_visualization_config = Column(JSON)
    mobile_optimized = Column(Boolean, default=False)
    accessibility_compliant = Column(Boolean, default=False)
    
    # Analytics and engagement
    views_count = Column(Integer, default=0)
    average_time_spent = Column(Float, default=0.0)  # in minutes
    user_feedback_score = Column(Float)  # 1-5 rating
    stakeholder_engagement_metrics = Column(JSON)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    published_at = Column(DateTime)
    last_reviewed_at = Column(DateTime)
    
    # Relationships
    organization = relationship("Organization", back_populates="esg_reports")
    user = relationship("User", back_populates="esg_reports")
    esg_score = relationship("ESGScore")
    
    def __repr__(self):
        return f"<ESGReport(org_id={self.organization_id}, title='{self.title}', status='{self.status}')>"
    
    @property
    def is_overdue(self) -> bool:
        """Check if report is overdue based on typical reporting cycles"""
        if self.status == ReportStatus.PUBLISHED:
            return False
        
        # Check if more than 30 days since creation without approval
        if self.status == ReportStatus.DRAFT:
            days_since_creation = (datetime.utcnow() - self.created_at).days
            return days_since_creation > 30
        
        return False
    
    @property
    def completeness_score(self) -> float:
        """Calculate report completeness score"""
        score = 0.0
        total_sections = 10
        
        # Check required sections
        if self.executive_summary:
            score += 1
        if self.environmental_section:
            score += 1
        if self.social_section:
            score += 1
        if self.governance_section:
            score += 1
        if self.ubuntu_section:
            score += 1
        if self.key_metrics:
            score += 1
        if self.targets_and_commitments:
            score += 1
        if self.materiality_assessment:
            score += 1
        if self.esg_risks_identified:
            score += 1
        if self.stakeholder_feedback:
            score += 1
        
        return (score / total_sections) * 100
    
    @property
    def african_context_rating(self) -> str:
        """Rate how well the report addresses African context"""
        african_score = 0
        
        # Check African-specific sections
        if self.ubuntu_section:
            african_score += 25
        if self.community_impact_section:
            african_score += 20
        if self.bee_compliance_section:
            african_score += 20
        if self.local_procurement_section:
            african_score += 15
        if self.cultural_preservation_section:
            african_score += 20
        
        if african_score >= 80:
            return "Excellent African Context"
        elif african_score >= 60:
            return "Good African Context"
        elif african_score >= 40:
            return "Moderate African Context"
        elif african_score >= 20:
            return "Limited African Context"
        else:
            return "Minimal African Context"
    
    def generate_report_summary(self) -> dict:
        """Generate a summary of the report for dashboard display"""
        return {
            "title": self.title,
            "type": self.report_type.value,
            "status": self.status.value,
            "completeness": self.completeness_score,
            "african_context": self.african_context_rating,
            "frameworks": self.frameworks_used,
            "is_verified": self.is_verified,
            "ubuntu_score": self.ubuntu_philosophy_score,
            "created_date": self.created_at.isoformat() if self.created_at else None,
            "published_date": self.published_at.isoformat() if self.published_at else None
        }