from fastapi import FastAPI, APIRouter

from llama_index.agent.openai import OpenAIAgent

from .chat import setup_chat_routes
from .database import setup_database_routes
from .files import setup_files_routes

from hive_agent.database.database import initialize_db


def setup_routes(app: FastAPI, agent: OpenAIAgent):

    @app.on_event("startup")
    async def startup_event():
        await initialize_db()

    @app.get("/")
    def read_root():
        return "Hive Agent is running"

    v1 = APIRouter()

    setup_chat_routes(v1, agent)
    setup_database_routes(v1)
    setup_files_routes(v1)

    app.include_router(v1, prefix="/api/v1")
