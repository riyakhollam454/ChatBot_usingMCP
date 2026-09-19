import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY","Addhere")
MCP_SERVER_HOST="127.0.0.1"
MCP_SERVER_PORT=8000
