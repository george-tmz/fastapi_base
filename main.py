import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.models.Users import User
from app.schemas import UserCreate
from config.app import settings
from core.DbConnect import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhased"
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/")
async def root(db: Session = Depends(get_db)):
    user = UserCreate
    user.email = "tmz@zyt.com"
    user.password = "123456"
    return create_user(db=db, user=user)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
