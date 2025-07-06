"""
ESGx.Africa API v1 Router
Main API router combining all endpoints
"""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    users,
    organizations,
    esg_scores,
    esg_reports,
    carbon_data,
    compliance,
    ai_agents,
    dashboard,
    ubuntu,
    analytics
)

api_router = APIRouter()

# Authentication and user management
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["Organizations"])

# ESG core functionality
api_router.include_router(esg_scores.router, prefix="/esg-scores", tags=["ESG Scores"])
api_router.include_router(esg_reports.router, prefix="/esg-reports", tags=["ESG Reports"])
api_router.include_router(carbon_data.router, prefix="/carbon", tags=["Carbon Data"])
api_router.include_router(compliance.router, prefix="/compliance", tags=["Compliance"])

# AI and Ubuntu features
api_router.include_router(ai_agents.router, prefix="/ai", tags=["AI Agents"])
api_router.include_router(ubuntu.router, prefix="/ubuntu", tags=["Ubuntu ESG"])

# Dashboard and analytics
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])