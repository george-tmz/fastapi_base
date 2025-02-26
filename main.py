import uvicorn
from fastapi import FastAPI
from config.app import settings
from core.DbConnect import SessionLocal, engine, Base

# create table
Base.metadata.create_all(bind=engine)
app = FastAPI()


# Get db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return "Welcome to here!"


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
