import asyncio

import uvicorn
from fastapi import FastAPI
from config.app import settings
from core.DbConnect import engine, Base
from routers import model
from core.RabbitMQConnect import  rabbitmq
from app.service.consumer import consume


# create table
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(model.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(consume())

@app.on_event("shutdown")
async def shutdown_event():
    await rabbitmq.close()

@app.get("/")
def root():
    return "Welcome to here!"

@app.post("/send_msg")
async def send_message_endpoint(message: str):
    await rabbitmq.publish("my_queue", message)
    return {"message": "Message sent!"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
