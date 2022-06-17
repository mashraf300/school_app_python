from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine('sqlite:///sqlite.db')
Session = sessionmaker(bind=db)

Base = declarative_base()

def setup_database():
	Base.metadata.create_all(db)


def session_factory():
    return Session()