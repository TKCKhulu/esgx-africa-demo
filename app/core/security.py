"""
ESGx.Africa Security Module
Authentication, Authorization, and Token Management
"""

from datetime import datetime, timedelta
from typing import Optional, Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.user import User

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT token handling
security = HTTPBearer()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generate password hash"""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            credentials.credentials, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception

def get_current_user(
    db: Session = Depends(get_db),
    username: str = Depends(verify_token)
) -> User:
    """Get current authenticated user"""
    user = db.query(User).filter(User.email == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

def check_subscription_access(required_plan: str):
    """Decorator to check if user has required subscription plan"""
    def decorator(current_user: User = Depends(get_current_user)):
        user_plan = current_user.subscription_plan
        
        # Plan hierarchy (higher index = more access)
        plan_hierarchy = [
            "community_free",
            "ubuntu_starter", 
            "growth_pro",
            "enterprise_esg",
            "enterprise_plus"
        ]
        
        if user_plan not in plan_hierarchy:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid subscription plan"
            )
            
        user_level = plan_hierarchy.index(user_plan)
        required_level = plan_hierarchy.index(required_plan)
        
        if user_level < required_level:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"This feature requires {required_plan} plan or higher"
            )
            
        return current_user
    return decorator

class UbuntuSecurityValidator:
    """Ubuntu-specific security validation for African ESG context"""
    
    @staticmethod
    def validate_african_context(data: dict) -> bool:
        """Validate that ESG data is appropriate for African context"""
        # Add Ubuntu/African-specific validation logic
        return True
    
    @staticmethod
    def check_bee_compliance(user: User) -> bool:
        """Check if user organization meets BEE requirements"""
        # Implement BEE compliance checking
        return True
    
    @staticmethod
    def validate_local_regulations(country_code: str, data: dict) -> bool:
        """Validate against local African regulations"""
        # Country-specific regulation checking
        african_countries = [
            "ZA", "KE", "NG", "GH", "UG", "TZ", "ZW", "BW", 
            "MW", "ZM", "MZ", "AO", "CI", "SN", "ML", "BF"
        ]
        return country_code in african_countries