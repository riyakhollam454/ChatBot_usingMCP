import asyncio, sys
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from gemini_agent import GeminiAgent

app = FastAPI()

# Mount static and template directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize Gemini Agent
agent = GeminiAgent()

class ChatRequest(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/chat")
async def chat_endpoint(data: ChatRequest):
    params = StdioServerParameters(command=sys.executable, args=["mcp_server.py"])

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = (await session.list_tools()).tools

            # Send input to Gemini with tools enabled
            response = agent.run_prompt_with_tools(data.prompt, tools)

            if response.function_calls:
                call = response.function_calls[0]
                result = await session.call_tool(call.name, call.args)
                
                output_text = ""
                for content in result.content:
                    if content.type == "text":
                        output_text += content.text

                return {
                    "status": "tool_execution",
                    "tool_name": call.name,
                    "tool_args": dict(call.args),
                    "result": output_text
                }
            else:
                return {
                    "status": "direct_response",
                    "response": response.text
                }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)