from fastapi import FastAPI
from backend.api.routes import router


app = FastAPI(
    title="OmniAI",
    version="0.1.0",
    description="Personal AI Framework"
)


app.include_router(router)