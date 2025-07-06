"""
ESGx.Africa AI Models for Skywork.ai Presentation
Advanced AI Architecture & Model Definitions

This file contains the AI model definitions that power the 47 neural networks
and 6 autonomous AI agents in the ESGx.Africa platform.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class AIModel(Base):
    """Core AI Model registry for all 47 neural networks"""
    __tablename__ = 'ai_models'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model_type = Column(String(50), nullable=False)  # Neural Network, Transformer, CNN, RNN, etc.
    version = Column(String(20), nullable=False)
    accuracy = Column(Float, nullable=False)
    confidence_score = Column(Float, nullable=False)
    training_data_size = Column(Integer, nullable=False)
    parameters_count = Column(Integer, nullable=False)
    status = Column(String(20), default='active')  # active, training, deployed, retired
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # AI Model Configuration
    hyperparameters = Column(JSON)
    training_config = Column(JSON)
    deployment_config = Column(JSON)
    
    # Performance Metrics
    processing_speed_ms = Column(Float)
    memory_usage_mb = Column(Float)
    cpu_usage_percent = Column(Float)
    
    # Competitive Advantages
    competitive_edge = Column(Text)
    unique_features = Column(JSON)
    
    # Relationships
    predictions = relationship("AIPrediction", back_populates="model")
    training_jobs = relationship("AITrainingJob", back_populates="model")
    performance_metrics = relationship("AIModelPerformance", back_populates="model")

class NeuralNetwork(Base):
    """Specialized Neural Network models for ESG analysis"""
    __tablename__ = 'neural_networks'
    
    id = Column(Integer, primary_key=True)
    ai_model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    network_architecture = Column(String(100), nullable=False)  # CNN, RNN, LSTM, Transformer, etc.
    layers_count = Column(Integer, nullable=False)
    neurons_count = Column(Integer, nullable=False)
    activation_function = Column(String(50), nullable=False)
    optimizer = Column(String(50), nullable=False)
    learning_rate = Column(Float, nullable=False)
    batch_size = Column(Integer, nullable=False)
    epochs = Column(Integer, nullable=False)
    
    # ESG-specific configurations
    esg_focus_area = Column(String(50))  # Environmental, Social, Governance, Ubuntu
    industry_specialization = Column(String(50))
    geographic_focus = Column(String(50))
    
    # Performance metrics
    training_accuracy = Column(Float)
    validation_accuracy = Column(Float)
    test_accuracy = Column(Float)
    f1_score = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    
    # Ubuntu integration
    ubuntu_integration_level = Column(Float)  # 0-1 scale
    cultural_context_awareness = Column(Float)  # 0-1 scale
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AIAgent(Base):
    """AI Agents for autonomous ESG operations"""
    __tablename__ = 'ai_agents'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    agent_type = Column(String(50), nullable=False)  # ESG_Analyzer, Risk_Assessor, etc.
    description = Column(Text)
    
    # Agent capabilities
    primary_function = Column(String(200))
    secondary_functions = Column(JSON)
    supported_languages = Column(JSON)
    automation_level = Column(Float)  # 0-1 scale (0.95 = 95% automation)
    
    # AI Model associations
    primary_model_id = Column(Integer, ForeignKey('ai_models.id'))
    supporting_models = Column(JSON)  # List of model IDs
    
    # Performance metrics
    tasks_completed_today = Column(Integer, default=0)
    success_rate = Column(Float)
    average_processing_time_ms = Column(Float)
    
    # Ubuntu integration
    ubuntu_philosophy_integration = Column(Float)  # 0-1 scale
    community_interaction_capability = Column(Boolean, default=False)
    
    # Status and configuration
    status = Column(String(20), default='active')  # active, idle, maintenance, training
    configuration = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    tasks = relationship("AIAgentTask", back_populates="agent")

class AIAgentTask(Base):
    """Tasks executed by AI agents"""
    __tablename__ = 'ai_agent_tasks'
    
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('ai_agents.id'), nullable=False)
    task_name = Column(String(200), nullable=False)
    task_type = Column(String(50), nullable=False)
    description = Column(Text)
    
    # Task execution details
    input_data = Column(JSON)
    output_data = Column(JSON)
    processing_time_ms = Column(Float)
    
    # Status and results
    status = Column(String(20), default='pending')  # pending, processing, completed, failed
    success = Column(Boolean)
    error_message = Column(Text)
    confidence_score = Column(Float)
    
    # Ubuntu context
    ubuntu_impact_score = Column(Float)  # How much this task impacts Ubuntu principles
    community_benefit_score = Column(Float)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    
    # Relationships
    agent = relationship("AIAgent", back_populates="tasks")

class AIPrediction(Base):
    """AI predictions and forecasts for ESG metrics"""
    __tablename__ = 'ai_predictions'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    company_id = Column(Integer, nullable=False)  # Reference to company
    
    # Prediction details
    prediction_type = Column(String(50), nullable=False)  # ESG_Score, Risk_Level, Ubuntu_Index
    predicted_value = Column(Float, nullable=False)
    confidence_interval_lower = Column(Float)
    confidence_interval_upper = Column(Float)
    confidence_score = Column(Float, nullable=False)
    
    # Time horizon
    prediction_horizon_days = Column(Integer, nullable=False)
    target_date = Column(DateTime, nullable=False)
    
    # Input features and context
    input_features = Column(JSON)
    market_conditions = Column(JSON)
    regulatory_environment = Column(JSON)
    
    # Ubuntu context
    ubuntu_factors = Column(JSON)
    cultural_context = Column(JSON)
    community_impact_prediction = Column(Float)
    
    # Validation and accuracy
    actual_value = Column(Float)  # Filled when prediction can be validated
    prediction_accuracy = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    validated_at = Column(DateTime)
    
    # Relationships
    model = relationship("AIModel", back_populates="predictions")

class AITrainingJob(Base):
    """AI model training jobs and experiments"""
    __tablename__ = 'ai_training_jobs'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    job_name = Column(String(200), nullable=False)
    job_type = Column(String(50), nullable=False)  # initial_training, retraining, fine_tuning
    
    # Training configuration
    training_data_size = Column(Integer)
    validation_data_size = Column(Integer)
    test_data_size = Column(Integer)
    
    # Hyperparameters
    hyperparameters = Column(JSON)
    
    # Training progress and results
    status = Column(String(20), default='queued')  # queued, running, completed, failed
    progress_percent = Column(Float, default=0.0)
    current_epoch = Column(Integer, default=0)
    total_epochs = Column(Integer)
    
    # Performance metrics
    training_loss = Column(Float)
    validation_loss = Column(Float)
    training_accuracy = Column(Float)
    validation_accuracy = Column(Float)
    
    # Ubuntu-specific metrics
    ubuntu_alignment_score = Column(Float)
    cultural_sensitivity_score = Column(Float)
    
    # Resource usage
    compute_hours = Column(Float)
    memory_peak_gb = Column(Float)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    
    # Relationships
    model = relationship("AIModel", back_populates="training_jobs")

class AIInsight(Base):
    """AI-generated insights and recommendations"""
    __tablename__ = 'ai_insights'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    company_id = Column(Integer, nullable=False)
    
    # Insight details
    insight_type = Column(String(50), nullable=False)  # risk_alert, opportunity, trend, anomaly
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    
    # Insight metrics
    importance_score = Column(Float, nullable=False)  # 0-1 scale
    confidence_score = Column(Float, nullable=False)  # 0-1 scale
    urgency_level = Column(String(20))  # low, medium, high, critical
    
    # Ubuntu context
    ubuntu_relevance = Column(Float)  # How relevant to Ubuntu principles
    community_impact = Column(Text)
    shared_value_potential = Column(Float)
    
    # Supporting data
    supporting_data = Column(JSON)
    data_sources = Column(JSON)
    
    # Recommendations
    recommended_actions = Column(JSON)
    expected_impact = Column(Text)
    
    # Validation
    human_validated = Column(Boolean, default=False)
    validation_score = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime)

class AIModelPerformance(Base):
    """Real-time AI model performance monitoring"""
    __tablename__ = 'ai_model_performance'
    
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    
    # Performance metrics
    timestamp = Column(DateTime, default=datetime.utcnow)
    accuracy = Column(Float)
    precision = Column(Float)
    recall = Column(Float)
    f1_score = Column(Float)
    
    # Processing metrics
    average_response_time_ms = Column(Float)
    throughput_requests_per_second = Column(Float)
    error_rate = Column(Float)
    
    # Resource utilization
    cpu_usage_percent = Column(Float)
    memory_usage_mb = Column(Float)
    gpu_usage_percent = Column(Float)
    
    # Ubuntu-specific metrics
    ubuntu_alignment_score = Column(Float)
    cultural_sensitivity_score = Column(Float)
    community_impact_score = Column(Float)
    
    # Drift detection
    data_drift_score = Column(Float)
    model_drift_score = Column(Float)
    
    # Relationships
    model = relationship("AIModel", back_populates="performance_metrics")

class UbuntuAI(Base):
    """Specialized Ubuntu philosophy AI model for cultural ESG scoring"""
    __tablename__ = 'ubuntu_ai'
    
    id = Column(Integer, primary_key=True)
    ai_model_id = Column(Integer, ForeignKey('ai_models.id'), nullable=False)
    
    # Ubuntu-specific configurations
    ubuntu_principle_weights = Column(JSON)  # Weights for different Ubuntu principles
    cultural_context_models = Column(JSON)  # Different cultural context models
    traditional_leader_input_weight = Column(Float)  # Weight given to traditional leader input
    
    # Community integration
    community_validation_enabled = Column(Boolean, default=True)
    community_feedback_integration = Column(Boolean, default=True)
    traditional_knowledge_integration = Column(Boolean, default=True)
    
    # Language and cultural capabilities
    supported_languages = Column(JSON)  # African languages supported
    cultural_nuance_understanding = Column(Float)  # 0-1 scale
    
    # Ubuntu scoring methodology
    ubuntu_scoring_algorithm = Column(String(100))
    shared_value_calculation_method = Column(String(100))
    community_impact_weighting = Column(JSON)
    
    # Performance in Ubuntu context
    ubuntu_prediction_accuracy = Column(Float)
    cultural_sensitivity_score = Column(Float)
    community_acceptance_rate = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AIModelOrchestration(Base):
    """AI model orchestration and coordination"""
    __tablename__ = 'ai_model_orchestration'
    
    id = Column(Integer, primary_key=True)
    orchestration_name = Column(String(200), nullable=False)
    description = Column(Text)
    
    # Model coordination
    primary_models = Column(JSON)  # List of primary model IDs
    supporting_models = Column(JSON)  # List of supporting model IDs
    model_execution_order = Column(JSON)  # Execution sequence
    
    # Orchestration logic
    decision_logic = Column(JSON)  # How models interact and make decisions
    consensus_mechanism = Column(String(100))  # How models reach consensus
    conflict_resolution = Column(String(100))  # How conflicts are resolved
    
    # Performance metrics
    orchestration_accuracy = Column(Float)
    average_execution_time_ms = Column(Float)
    success_rate = Column(Float)
    
    # Ubuntu integration
    ubuntu_consensus_weight = Column(Float)  # Weight given to Ubuntu AI in consensus
    cultural_override_enabled = Column(Boolean, default=True)
    
    # Status and configuration
    status = Column(String(20), default='active')
    configuration = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Sample data for Skywork.ai presentation
SAMPLE_AI_MODELS = [
    {
        "name": "Ubuntu Neural Engine",
        "model_type": "Deep Learning",
        "accuracy": 98.7,
        "parameters_count": 175000000,
        "competitive_edge": "Only culturally-aware ESG AI in existence",
        "processing_speed_ms": 2.1
    },
    {
        "name": "ESG Sentiment Analyzer",
        "model_type": "NLP Transformer",
        "accuracy": 96.4,
        "parameters_count": 110000000,
        "competitive_edge": "8+ African languages, real-time processing",
        "processing_speed_ms": 1.8
    },
    {
        "name": "Risk Prediction Model",
        "model_type": "Ensemble ML",
        "accuracy": 94.8,
        "parameters_count": 50000000,
        "competitive_edge": "12-month forecasting vs industry 3-month",
        "processing_speed_ms": 2.5
    },
    {
        "name": "Satellite Vision AI",
        "model_type": "Computer Vision",
        "accuracy": 97.2,
        "parameters_count": 89000000,
        "competitive_edge": "Real-time environmental verification",
        "processing_speed_ms": 3.2
    },
    {
        "name": "Investment Scoring AI",
        "model_type": "Reinforcement Learning",
        "accuracy": 95.9,
        "parameters_count": 75000000,
        "competitive_edge": "Cultural impact assessment unique globally",
        "processing_speed_ms": 2.8
    }
]

SAMPLE_AI_AGENTS = [
    {
        "name": "ESG Data Extraction Agent",
        "agent_type": "Data_Processor",
        "automation_level": 0.95,
        "tasks_completed_today": 2847,
        "success_rate": 0.987
    },
    {
        "name": "Investment Screening Agent",
        "agent_type": "Investment_Analyzer",
        "automation_level": 0.88,
        "tasks_completed_today": 1653,
        "success_rate": 0.941
    },
    {
        "name": "Compliance Automation Agent",
        "agent_type": "Compliance_Monitor",
        "automation_level": 0.92,
        "tasks_completed_today": 934,
        "success_rate": 0.958
    },
    {
        "name": "Ubuntu Verification Agent",
        "agent_type": "Cultural_Validator",
        "automation_level": 0.85,
        "tasks_completed_today": 567,
        "success_rate": 0.923
    },
    {
        "name": "Risk Assessment Agent",
        "agent_type": "Risk_Analyzer",
        "automation_level": 0.89,
        "tasks_completed_today": 1234,
        "success_rate": 0.934
    },
    {
        "name": "Predictive Intelligence Agent",
        "agent_type": "Forecasting_Engine",
        "automation_level": 0.91,
        "tasks_completed_today": 789,
        "success_rate": 0.967
    }
]