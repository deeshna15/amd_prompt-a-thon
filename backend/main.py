from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .api import tools_router, workflow_router
import os
from dotenv import load_dotenv

load_dotenv()

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NutriMind AI API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tools_router.router, prefix="/api/tools", tags=["MCP Tools"])
app.include_router(workflow_router.router, prefix="/api/workflow", tags=["Workflow"])

@app.get("/")
def read_root():
    return {"message": "Welcome to NutriMind AI"}
