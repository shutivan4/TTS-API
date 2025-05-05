
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import edge_tts
import uuid
import asyncio

app = FastAPI()

@app.post("/tts")
async def tts(req: Request):
    body = await req.json()
    text = body.get("text", "Hello, world")
    voice = body.get("voice", "en-US-GuyNeural")
    rate = body.get("rate", "0%")
    pitch = body.get("pitch", "0%")

    filename = f"/tmp/{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename, rate=rate, pitch=pitch)
    return FileResponse(filename, media_type="audio/mpeg", filename="voice.mp3")
