from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://ADMIN:ADMIN@192.168.1.20:5432/aiproject"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()


def get_database():
    db = session_local()
    try:
        yield db
    except:
        db.close()
