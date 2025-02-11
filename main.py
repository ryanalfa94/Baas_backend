from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from database import users_collection
from auth import create_access_token, hash_password, verify_password
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

@app.get("/")
def home():
    return {"mesage": "Fast API is working"}


#define a pydentic model for request validation 
class UserSignup(BaseModel):
    name: str
    email: EmailStr      # Ensures a valid email format
    password: str

#### Signup API ####
@app.post("/signup/")
def signup (user:UserSignup):
    #check if  the user exists already
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="email already registered")
    
    #hash the password 
    hashed_password = hash_password(user.password)
    
    #now we save user data 
    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    })
    
    
    return {"message": "User registered successfully"}


#### Signin API ####
@app.post("/login/")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"email": form_data.username})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # Generate JWT token
    access_token = create_access_token({"sub": user["email"]})
    
    return {"access_token": access_token, "token_type": "bearer"}
     
