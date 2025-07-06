"""
ESGx.Africa - AI-Powered ESG Intelligence Platform for Africa
Main FastAPI application entry point
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import os
from pathlib import Path

# Import our modules
from app.core.config import settings
from app.api.v1.api import api_router
from app.db.session import engine
from app.db.base import Base
from app.core.security import verify_token

# Create FastAPI app
app = FastAPI(
    title="ESGx.Africa",
    description="AI-Powered ESG Intelligence Platform for Africa",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

# Security
security = HTTPBearer()

# Create database tables
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Health check
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "platform": "ESGx.Africa"}

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with platform info"""
    return {
        "message": "Welcome to ESGx.Africa",
        "description": "AI-Powered ESG Intelligence for Africa",
        "version": "1.0.0",
        "features": [
            "Ubuntu ESG Scoring",
            "AI ESG Agents",
            "Real-time Compliance Monitoring",
            "Carbon Accounting",
            "Multilingual Support",
            "White-label Solutions"
        ]
    }

# Static files for frontend (if serving React build)
if os.path.exists("frontend/build"):
    app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")
    
    @app.get("/app/{path:path}")
    async def serve_frontend(path: str):
        """Serve React frontend"""
        file_path = Path("frontend/build") / path
        if file_path.exists() and file_path.is_file():
            return FileResponse(file_path)
        return FileResponse("frontend/build/index.html")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )