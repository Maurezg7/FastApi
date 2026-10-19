from fastapi import APIRouter
import httpx
from pydantic import BaseModel

router = APIRouter(prefix='/llm', tags=["llm"])

class Question(BaseModel):
    prompt: str

@router.post("/ask")
async def askQuestion(question: Question):
    async with httpx.AsyncClient(timeout=600) as client:
        response = await client.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "qwen2.5:1.5b",
                "messages": [{"role": "user", "content": question.prompt}],
                "stream": False
            }
        )
    data = response.json()
    print("STATUS:", response.status_code)
    print("OLLAMA RESPONDIÓ:", data)   # 👈 esto te dice la verdad
    return data