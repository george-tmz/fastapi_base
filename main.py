import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.Users import User
from app.schemas import UserCreate
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
async def root(db: Session = Depends(get_db)):
    user = UserCreate
    user.email = "tmz@zyt.com"
    user.password = "123456"
    return create_user(db=db, user=user)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
