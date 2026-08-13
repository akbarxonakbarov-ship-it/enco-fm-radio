import os

from fastapi import FastAPI

app = FastAPI(title="Enco FM Radio")


@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "Enco FM Radio",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }