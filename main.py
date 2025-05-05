from fastapi import FastAPI
from pydantic import BaseModel
import edge_tts
import asyncio

app = FastAPI()

class TTSRequest(BaseModel):
    text: str
    voice: str = "en-US-GuyNeural"
    rate: str = "-30%"
    pitch: str = "-10%"

@app.post("/tts")
async def tts(req: TTSRequest):
    communicate = edge_tts.Communicate(
        text=req.text,
        voice=req.voice,
        rate=req.rate,
        pitch=req.pitch
    )
    output_path = "output.mp3"
    await communicate.save(output_path)
    return {"message": "TTS completed", "file": output_path}