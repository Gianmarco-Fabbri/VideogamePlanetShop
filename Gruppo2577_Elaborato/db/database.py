from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

def setup_database():
    engine = create_engine('mysql+mysqlclient://username:password@host:port/dbname')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return engine, Session