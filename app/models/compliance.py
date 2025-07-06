"""
ESGx.Africa Compliance Record Model
Tracking regulatory compliance across African jurisdictions
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey, Boolean, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime, timedelta
import enum

from app.db.session import Base

class ComplianceFramework(str, enum.Enum):
    """Compliance frameworks and regulations"""
    BEE = "bee"  # Broad-Based Black Economic Empowerment
    JSE = "jse"  # Johannesburg Stock Exchange
    GRI = "gri"  # Global Reporting Initiative
    SASB = "sasb"  # Sustainability Accounting Standards Board
    TCFD = "tcfd"  # Task Force on Climate-related Financial Disclosures
    ISO14001 = "iso14001"  # Environmental Management
    ISO45001 = "iso45001"  # Occupational Health and Safety
    CSIR = "csir"  # Council for Scientific and Industrial Research
    SDG = "sdg"  # UN Sustainable Development Goals
    KING_IV = "king_iv"  # King IV Corporate Governance
    NEMA = "nema"  # National Environmental Management Act (SA)
    MPRDA = "mprda"  # Mineral and Petroleum Resources Development Act
    LOCAL_REGULATION = "local_regulation"  # Country-specific regulations

class ComplianceStatus(str, enum.Enum):
    """Compliance status levels"""
    COMPLIANT = "compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    UNDER_REVIEW = "under_review"
    PENDING_SUBMISSION = "pending_submission"
    NOT_APPLICABLE = "not_applicable"

class RiskLevel(str, enum.Enum):
    """Risk levels for compliance issues"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class ComplianceRecord(Base):
    """Compliance record model for tracking regulatory adherence"""
    __tablename__ = "compliance_records"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Compliance officer
    
    # Compliance framework details
    framework = Column(SQLEnum(ComplianceFramework), nullable=False)
    framework_version = Column(String)  # Version of the framework/regulation
    regulation_name = Column(String, nullable=False)
    regulation_code = Column(String)  # Official regulation code/number
    
    # Geographic and jurisdictional
    country_code = Column(String, nullable=False)
    province_state = Column(String)
    regulator_name = Column(String)  # Name of regulatory body
    
    # Compliance status
    status = Column(SQLEnum(ComplianceStatus), nullable=False)
    compliance_percentage = Column(Float, default=0.0)  # 0-100%
    risk_level = Column(SQLEnum(RiskLevel), default=RiskLevel.LOW)
    
    # Assessment details
    assessment_date = Column(DateTime, nullable=False)
    assessment_method = Column(String)  # self-assessment, third-party, audit
    assessor_name = Column(String)
    assessment_score = Column(Float)  # Overall assessment score
    
    # Requirements and criteria
    total_requirements = Column(Integer, default=0)
    met_requirements = Column(Integer, default=0)
    partially_met_requirements = Column(Integer, default=0)
    unmet_requirements = Column(Integer, default=0)
    
    # Detailed compliance breakdown
    requirements_breakdown = Column(JSON)  # Detailed requirement by requirement
    evidence_provided = Column(JSON)  # Evidence for each requirement
    gaps_identified = Column(JSON)  # Non-compliance gaps
    
    # African-specific compliance areas
    bee_scorecard = Column(JSON)  # BEE scorecard details
    local_content_percentage = Column(Float)  # Local content compliance
    community_benefit_score = Column(Float)  # Community benefit compliance
    indigenous_rights_compliance = Column(Boolean, default=True)
    land_rights_compliance = Column(Boolean, default=True)
    
    # Certification and verification
    certificate_number = Column(String)
    certificate_issued_date = Column(DateTime)
    certificate_expiry_date = Column(DateTime)
    certification_body = Column(String)
    is_certificate_valid = Column(Boolean, default=False)
    
    # Reporting and disclosure
    last_reported_date = Column(DateTime)
    next_reporting_due_date = Column(DateTime)
    reporting_frequency = Column(String)  # annual, quarterly, monthly
    public_disclosure_required = Column(Boolean, default=False)
    disclosure_url = Column(String)
    
    # Penalties and enforcement
    penalties_incurred = Column(JSON)  # Details of any penalties
    total_penalty_amount = Column(Float, default=0.0)
    enforcement_actions = Column(JSON)  # Enforcement actions taken
    corrective_actions_required = Column(JSON)
    
    # Improvement and action plans
    action_plan = Column(JSON)  # Action plan to address gaps
    improvement_targets = Column(JSON)  # Specific improvement targets
    responsible_persons = Column(JSON)  # People responsible for compliance
    budget_allocated = Column(Float)  # Budget for compliance improvements
    
    # Monitoring and tracking
    monitoring_frequency = Column(String)  # How often compliance is monitored
    key_performance_indicators = Column(JSON)  # KPIs for compliance
    trend_analysis = Column(JSON)  # Compliance trend over time
    benchmark_comparison = Column(JSON)  # Comparison with industry benchmarks
    
    # AI-powered insights
    ai_risk_assessment = Column(JSON)  # AI-generated risk assessment
    ai_recommendations = Column(JSON)  # AI recommendations for improvement
    predictive_compliance_score = Column(Float)  # Predicted future compliance
    
    # Stakeholder communication
    stakeholder_notifications = Column(JSON)  # Stakeholder communication log
    regulator_communications = Column(JSON)  # Communications with regulators
    public_commitments = Column(JSON)  # Public commitments made
    
    # Cost and resource tracking
    compliance_costs = Column(Float, default=0.0)  # Total compliance costs
    staff_time_allocated = Column(Float)  # Staff hours allocated
    external_consultant_costs = Column(Float, default=0.0)
    training_costs = Column(Float, default=0.0)
    
    # Document management
    supporting_documents = Column(JSON)  # List of supporting documents
    policy_documents = Column(JSON)  # Related policy documents
    training_records = Column(JSON)  # Training records
    audit_trail = Column(JSON)  # Audit trail of changes
    
    # Review and approval
    reviewed_by = Column(String)  # Who reviewed the compliance record
    approved_by = Column(String)  # Who approved the compliance record
    review_date = Column(DateTime)
    approval_date = Column(DateTime)
    review_comments = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization", back_populates="compliance_records")
    user = relationship("User")
    
    def __repr__(self):
        return f"<ComplianceRecord(org_id={self.organization_id}, framework='{self.framework}', status='{self.status}')>"
    
    @property
    def is_certificate_expiring_soon(self) -> bool:
        """Check if certificate is expiring within 90 days"""
        if not self.certificate_expiry_date:
            return False
        
        warning_date = datetime.utcnow() + timedelta(days=90)
        return self.certificate_expiry_date <= warning_date
    
    @property
    def is_reporting_overdue(self) -> bool:
        """Check if reporting is overdue"""
        if not self.next_reporting_due_date:
            return False
        
        return datetime.utcnow() > self.next_reporting_due_date
    
    @property
    def compliance_grade(self) -> str:
        """Get compliance grade based on percentage"""
        if self.compliance_percentage >= 95:
            return "A+"
        elif self.compliance_percentage >= 90:
            return "A"
        elif self.compliance_percentage >= 85:
            return "A-"
        elif self.compliance_percentage >= 80:
            return "B+"
        elif self.compliance_percentage >= 75:
            return "B"
        elif self.compliance_percentage >= 70:
            return "B-"
        elif self.compliance_percentage >= 65:
            return "C+"
        elif self.compliance_percentage >= 60:
            return "C"
        elif self.compliance_percentage >= 55:
            return "C-"
        else:
            return "F"
    
    @property
    def priority_level(self) -> str:
        """Determine priority level based on risk and compliance status"""
        if self.risk_level == RiskLevel.CRITICAL:
            return "Critical"
        elif self.status == ComplianceStatus.NON_COMPLIANT and self.risk_level == RiskLevel.HIGH:
            return "High"
        elif self.is_certificate_expiring_soon or self.is_reporting_overdue:
            return "High"
        elif self.status == ComplianceStatus.PARTIALLY_COMPLIANT:
            return "Medium"
        else:
            return "Low"
    
    def calculate_african_context_score(self) -> float:
        """Calculate score based on African-specific compliance factors"""
        score = 0.0
        
        # BEE compliance (if applicable)
        if self.framework == ComplianceFramework.BEE and self.status == ComplianceStatus.COMPLIANT:
            score += 30
        
        # Local content compliance
        if self.local_content_percentage and self.local_content_percentage > 50:
            score += 25
        elif self.local_content_percentage and self.local_content_percentage > 25:
            score += 15
        
        # Community benefit compliance
        if self.community_benefit_score and self.community_benefit_score > 75:
            score += 25
        elif self.community_benefit_score and self.community_benefit_score > 50:
            score += 15
        
        # Indigenous and land rights compliance
        if self.indigenous_rights_compliance:
            score += 10
        if self.land_rights_compliance:
            score += 10
        
        return min(score, 100.0)  # Cap at 100