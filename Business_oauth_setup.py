from fastapi import FastAPI, APIRouter, Request
import requests
import psycopg2
import os
from dotenv import load_dotenv

app = FastAPI()

# Load environment variables from .env
load_dotenv()

# Create a FastAPI Router
router = APIRouter()

# OAuth Callback Route
@router.get("/oauth/callback")
async def oauth_callback(request: Request):
    params = request.query_params
    code = params.get("code")
    state = params.get("state")

    if not code:
        return {"error": "Authorization code not found"}

    print("Received Authorization Code:", code)
    print("Received State:", state)

# Include the router
app.include_router(router)
