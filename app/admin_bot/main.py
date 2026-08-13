import os

from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update

from app.config import settings
from app.database.session import init_db
from app.admin_bot.handlers import router


app = FastAPI()

bot = Bot(token=settings.bot_token)
dp = Dispatcher()
dp.include_router(router)


@app.on_event("startup")
async def startup():
    await init_db()

    webhook_url = os.environ["WEBHOOK_URL"]
    await bot.set_webhook(webhook_url)

    print("Enco FM Database Bot started")


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)

    await dp.feed_update(bot, update)

    return {"ok": True}


@app.get("/")
async def health():
    return {"status": "ok", "service": "Enco FM Database Bot"}


@app.on_event("shutdown")
async def shutdown():
    await bot.delete_webhook()
    await bot.session.close()