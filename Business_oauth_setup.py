# from fastapi import FastAPI, APIRouter, Request
# import requests
# import psycopg2
# import os
# from dotenv import load_dotenv

# app = FastAPI()

# # Load environment variables from .env
# load_dotenv()

# # Create a FastAPI Router
# router = APIRouter()

# # OAuth Callback Route
# @router.get("/oauth/callback")
# async def oauth_callback(request: Request):
#     params = request.query_params
#     code = params.get("code")
#     state = params.get("state")

#     if not code:
#         return {"error": "Authorization code not found"}

#     print("Received Authorization Code:", code)
#     print("Received State:", state)

# # Include the router
# app.include_router(router)
from fastapi import FastAPI, APIRouter, Request
import requests
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set server details (host and port)
HOST = os.getenv("SERVER_HOST", "0.0.0.0")
PORT = int(os.getenv("SERVER_PORT", 8000))

# Create a FastAPI app
app = FastAPI()

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
    return {"message": "OAuth authorization successful! You can close this page."}

# Include the router
app.include_router(router)

# Only print server info if running directly (not when imported)
if __name__ == "__main__":
    print(f"Starting FastAPI server at http://{HOST}:{PORT}")
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)

