import uvicorn
from fastapi import FastAPI

from config.app import settings
from core.DbConnect import SessionLocal, engine, Base
from routers import model

# create table
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(model.router)


@app.get("/")
def root():
    return "Welcome to here!"


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
