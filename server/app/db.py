from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import settings 


engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
