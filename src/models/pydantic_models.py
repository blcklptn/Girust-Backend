from sqlalchemy import Column, String, Integer

from database.db import Base

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    password_hash = Column(String)
