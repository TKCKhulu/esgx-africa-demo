"""
ESGx.Africa AI Agent Models
Ubuntu GPT-powered ESG Intelligence
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey, Boolean, Text, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum

from app.db.session import Base

class AgentType(str, enum.Enum):
    """Types of AI agents available in ESGx.Africa"""
    UBUNTU_ESG_ADVISOR = "ubuntu_esg_advisor"  # General ESG guidance with Ubuntu context
    COMPLIANCE_ASSISTANT = "compliance_assistant"  # Regulatory compliance help
    CARBON_CALCULATOR = "carbon_calculator"  # Carbon footprint analysis
    BEE_ANALYZER = "bee_analyzer"  # BEE compliance analysis
    RISK_ASSESSOR = "risk_assessor"  # ESG risk assessment
    REPORT_GENERATOR = "report_generator"  # Automated report generation
    BENCHMARK_ANALYST = "benchmark_analyst"  # Industry benchmarking
    SUSTAINABILITY_COACH = "sustainability_coach"  # Improvement recommendations

class ConversationStatus(str, enum.Enum):
    """Status of AI conversations"""
    ACTIVE = "active"
    COMPLETED = "completed"
    ARCHIVED = "archived"
    ERROR = "error"

class AIAgent(Base):
    """AI Agent model for ESGx.Africa platform"""
    __tablename__ = "ai_agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    agent_type = Column(SQLEnum(AgentType), nullable=False)
    
    # Agent configuration
    model_version = Column(String, default="gpt-4")  # Ubuntu GPT model
    system_prompt = Column(Text, nullable=False)
    temperature = Column(Float, default=0.7)
    max_tokens = Column(Integer, default=2000)
    
    # African/Ubuntu context configuration
    ubuntu_context_enabled = Column(Boolean, default=True)
    african_regulations_enabled = Column(Boolean, default=True)
    local_language_support = Column(JSON)  # Supported languages
    cultural_context = Column(JSON)  # Cultural context data
    
    # Capabilities and features
    capabilities = Column(JSON)  # List of agent capabilities
    supported_frameworks = Column(JSON)  # ESG frameworks this agent supports
    data_sources = Column(JSON)  # Data sources the agent can access
    
    # Usage and performance
    total_conversations = Column(Integer, default=0)
    average_satisfaction_score = Column(Float, default=0.0)
    success_rate = Column(Float, default=0.0)
    
    # Access control
    subscription_plans_allowed = Column(JSON)  # Which plans can use this agent
    is_active = Column(Boolean, default=True)
    is_beta = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
    # Relationships
    conversations = relationship("AIConversation", back_populates="agent")
    
    def __repr__(self):
        return f"<AIAgent(name='{self.name}', type='{self.agent_type}')>"

class AIConversation(Base):
    """AI Conversation model for tracking user interactions with agents"""
    __tablename__ = "ai_conversations"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relationships
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    agent_id = Column(Integer, ForeignKey("ai_agents.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    
    # Conversation metadata
    title = Column(String, nullable=False)
    status = Column(SQLEnum(ConversationStatus), default=ConversationStatus.ACTIVE)
    language = Column(String, default="en")
    
    # Conversation data
    messages = Column(JSON, nullable=False)  # Full conversation history
    context = Column(JSON)  # Conversation context and variables
    ubuntu_context_applied = Column(Boolean, default=False)
    
    # ESG-specific context
    esg_topic = Column(String)  # Main ESG topic being discussed
    frameworks_discussed = Column(JSON)  # ESG frameworks mentioned
    compliance_areas = Column(JSON)  # Compliance areas covered
    
    # Performance metrics
    user_satisfaction_score = Column(Float)  # 1-5 rating
    response_time_avg = Column(Float)  # Average response time in seconds
    resolution_achieved = Column(Boolean, default=False)
    
    # Usage tracking
    total_messages = Column(Integer, default=0)
    total_tokens_used = Column(Integer, default=0)
    cost_estimate = Column(Float, default=0.0)  # Estimated cost in USD
    
    # AI insights generated
    insights_generated = Column(JSON)  # Key insights from conversation
    recommendations = Column(JSON)  # Recommendations provided
    action_items = Column(JSON)  # Action items identified
    
    # Follow-up and scheduling
    follow_up_scheduled = Column(Boolean, default=False)
    follow_up_date = Column(DateTime)
    follow_up_topic = Column(String)
    
    # Timestamps
    started_at = Column(DateTime, server_default=func.now())
    last_message_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime)
    
    # Relationships
    user = relationship("User", back_populates="ai_conversations")
    agent = relationship("AIAgent", back_populates="conversations")
    
    def __repr__(self):
        return f"<AIConversation(user_id={self.user_id}, agent='{self.agent.name}', status='{self.status}')>"
    
    def add_message(self, role: str, content: str, metadata: dict = None):
        """Add a new message to the conversation"""
        if self.messages is None:
            self.messages = []
        
        message = {
            "role": role,  # "user", "assistant", "system"
            "content": content,
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        
        self.messages.append(message)
        self.total_messages += 1
        self.last_message_at = datetime.utcnow()
    
    @property
    def conversation_duration(self) -> float:
        """Get conversation duration in minutes"""
        if self.completed_at:
            return (self.completed_at - self.started_at).total_seconds() / 60
        return (datetime.utcnow() - self.started_at).total_seconds() / 60
    
    @property
    def ubuntu_insights_count(self) -> int:
        """Count Ubuntu-specific insights generated"""
        if not self.insights_generated:
            return 0
        return len([insight for insight in self.insights_generated 
                   if "ubuntu" in insight.get("tags", [])])

class AIAgentTemplate:
    """Template configurations for different AI agents"""
    
    UBUNTU_ESG_ADVISOR = {
        "name": "Ubuntu ESG Advisor",
        "agent_type": AgentType.UBUNTU_ESG_ADVISOR,
        "system_prompt": """You are an Ubuntu ESG Advisor for ESGx.Africa, helping organizations integrate African Ubuntu philosophy with modern ESG practices. You understand the importance of community (Ubuntu), environmental stewardship in African contexts, and culturally-appropriate governance structures. 

Your expertise includes:
- Ubuntu philosophy and its application to ESG
- African regulatory frameworks (BEE, JSE, local laws)
- Community-centered sustainability approaches
- African environmental challenges and solutions
- Indigenous knowledge systems
- Local procurement and community investment

Always consider the African context and provide culturally-sensitive advice that respects Ubuntu values while meeting international ESG standards.""",
        "capabilities": [
            "Ubuntu philosophy integration",
            "African ESG frameworks",
            "Community engagement strategies",
            "BEE compliance guidance",
            "Cultural context analysis"
        ],
        "supported_frameworks": ["GRI", "SASB", "TCFD", "BEE", "SDG", "JSE"],
        "subscription_plans_allowed": ["ubuntu_starter", "growth_pro", "enterprise_esg", "enterprise_plus"]
    },
    
    COMPLIANCE_ASSISTANT = {
        "name": "Compliance Assistant",
        "agent_type": AgentType.COMPLIANCE_ASSISTANT,
        "system_prompt": """You are a Compliance Assistant specializing in African ESG regulations and international standards. You help organizations navigate complex regulatory requirements across African countries, with deep knowledge of local laws, BEE requirements, JSE listing rules, and international ESG standards.

Your expertise covers:
- African country-specific regulations
- BEE compliance requirements
- JSE sustainability reporting
- International ESG frameworks
- Risk assessment and mitigation
- Audit preparation and documentation

Provide clear, actionable compliance guidance while considering resource constraints common in African markets.""",
        "capabilities": [
            "Regulatory compliance checking",
            "BEE analysis",
            "JSE reporting requirements",
            "Risk assessment",
            "Audit preparation"
        ],
        "supported_frameworks": ["BEE", "JSE", "GRI", "TCFD", "ISO14001", "ISO45001"],
        "subscription_plans_allowed": ["growth_pro", "enterprise_esg", "enterprise_plus"]
    }
}