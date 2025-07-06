"""
ESGx.Africa Configuration Management
"""

import os
from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Application settings"""
    
    # App Info
    APP_NAME: str = "ESGx.Africa"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = Field(default=False, env="DEBUG")
    
    # Security
    SECRET_KEY: str = Field(env="SECRET_KEY", default="your-secret-key-change-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"
    
    # Database
    DATABASE_URL: str = Field(
        env="DATABASE_URL",
        default="postgresql://esgx_user:esgx_password@localhost/esgx_africa"
    )
    
    # Redis (for caching and background tasks)
    REDIS_URL: str = Field(env="REDIS_URL", default="redis://localhost:6379")
    
    # AI/OpenAI Configuration
    OPENAI_API_KEY: Optional[str] = Field(env="OPENAI_API_KEY", default=None)
    UBUNTU_GPT_MODEL: str = "gpt-4"  # Ubuntu-trained model
    
    # ESG Data Sources
    ESG_DATA_API_KEY: Optional[str] = Field(env="ESG_DATA_API_KEY", default=None)
    CARBON_API_KEY: Optional[str] = Field(env="CARBON_API_KEY", default=None)
    
    # File Storage
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    
    # Email Configuration
    SMTP_HOST: Optional[str] = Field(env="SMTP_HOST", default=None)
    SMTP_PORT: int = Field(env="SMTP_PORT", default=587)
    SMTP_USER: Optional[str] = Field(env="SMTP_USER", default=None)
    SMTP_PASSWORD: Optional[str] = Field(env="SMTP_PASSWORD", default=None)
    
    # Subscription Plans (in South African Rand)
    SUBSCRIPTION_PLANS: dict = {
        "community_free": {
            "name": "Community Free",
            "price_monthly": 0,
            "price_annual": 0,
            "features": ["Ubuntu Index™", "SMS input", "3 reports/month"],
            "max_reports": 3,
            "ai_agents": 0
        },
        "ubuntu_starter": {
            "name": "Ubuntu Starter", 
            "price_monthly": 2500,
            "price_annual": 25000,
            "features": ["Core ESG KPIs", "ESG wizard", "email support"],
            "max_reports": 50,
            "ai_agents": 1
        },
        "growth_pro": {
            "name": "Growth Pro",
            "price_monthly": 15000,
            "price_annual": 150000,
            "features": ["2 AI agents", "JSE compliance", "ESGx metrics"],
            "max_reports": 500,
            "ai_agents": 2
        },
        "enterprise_esg": {
            "name": "Enterprise ESG",
            "price_monthly": 75000,
            "price_annual": 750000,
            "features": ["All AI agents", "API access", "custom reporting"],
            "max_reports": -1,  # unlimited
            "ai_agents": 5
        },
        "enterprise_plus": {
            "name": "Enterprise+",
            "price_monthly": 150000,  # average
            "price_annual": 1500000,
            "features": ["On-premise", "white-labeling", "dedicated AI & support"],
            "max_reports": -1,  # unlimited
            "ai_agents": -1  # unlimited
        }
    }
    
    # African Languages Support
    SUPPORTED_LANGUAGES: List[str] = [
        "en",  # English
        "af",  # Afrikaans
        "zu",  # Zulu
        "xh",  # Xhosa
        "sw",  # Swahili
        "fr",  # French
        "pt",  # Portuguese
        "ar",  # Arabic
    ]
    
    # ESG Framework Standards
    ESG_FRAMEWORKS: List[str] = [
        "GRI",      # Global Reporting Initiative
        "SASB",     # Sustainability Accounting Standards Board
        "TCFD",     # Task Force on Climate-related Financial Disclosures
        "CSIR",     # Council for Scientific and Industrial Research
        "BEE",      # Broad-Based Black Economic Empowerment
        "SDG",      # Sustainable Development Goals
        "ISO14001", # Environmental Management
        "ISO45001", # Occupational Health and Safety
        "JSE",      # Johannesburg Stock Exchange requirements
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()