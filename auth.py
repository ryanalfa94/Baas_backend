from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone  
from jose import JWTError, jwt
import os
from dotenv import load_dotenv



# Create a password hashing object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_pasword: str, hashed_password: str) -> bool:
    """Verifies a password against the stored hashed password."""
    return pwd_context.verify(plain_pasword,hashed_password)


# Load SECRET_KEY securely from .env
SECRET_KEY = os.getenv("SECRET_KEY")

# Fallback in case SECRET_KEY is missing (optional)
if SECRET_KEY is None:
    raise ValueError("SECRET_KEY is missing! Please set it in the .env file.")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)