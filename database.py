#model

from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)


#database

from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "user://user:password@localhost:5432/user"

engine = create_engine(DATABASE_URL )
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()






