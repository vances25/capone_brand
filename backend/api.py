from fastapi import FastAPI, HTTPException, Request
import asyncio
import uvicorn
from pydantic import BaseModel
from telegram import Bot
import os
from fastapi.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from dotenv import load_dotenv
load_dotenv()



TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")

SECRET_KEY = os.getenv("SECRET_KEY")

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(redoc_url=None, docs_url=None)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = Bot(token=TELEGRAM_TOKEN)


telegram_link = ""
instagram_link = ""


class Update(BaseModel):
    telegram: str | None = None
    instagram: str | None = None
    key: str
@app.post("/update")
async def update(data: Update):
    global telegram_link, instagram_link
    
    if data.key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="you are not permited")
    
    if data.telegram:
        telegram_link = data.telegram
        
    if data.instagram:
        instagram_link = data.instagram
    
    return {"message": "succesfully changed link"}

@app.get("/socials")
async def socials():
    global telegram_link, instagram_link
    return {"telegram": telegram_link, "instagram": instagram_link}

class RequestNumber(BaseModel):
    username: str
    phone: str
@app.post("/request_number")
@limiter.limit("5/minute")
async def request_number(data: RequestNumber, request: Request):
    global bot
    
    await bot.send_message(chat_id=CHAT_ID, text=f"🔔 Someone wants to connect!\n\nName: {data.username}\nPhone:{data.phone}\n\nYou just got a new contact request. Let’s go!")
    return {"data":"success, please give us a moment and we will reach out soon!"}

async def main():
    global app
    global tele_app

    config = uvicorn.Config(app, host="0.0.0.0", port=5050)
    server = uvicorn.Server(config)
    await server.serve()
    




if __name__ == "__main__":
   asyncio.run(main())