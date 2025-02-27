from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.database import Db


DATABASE_URI = f"mysql+pymysql://{Db.DB_USER}:{Db.DB_PASSWORD}@{Db.DB_HOST}:{Db.DB_PORT}/{Db.DB_NAME}"

engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
