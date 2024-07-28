from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from config.settings import settings

app = FastAPI()

# Define the static token
STATIC_TOKEN = settings.AUTH_TOKEN


# Dependency to check the token
def get_token(token: str = Depends(HTTPBearer())):
    if token.credentials != STATIC_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"Authorization": "Bearer"},
        )
    return token.credentials
