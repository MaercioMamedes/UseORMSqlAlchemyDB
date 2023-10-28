from sqlalchemy import create_engine
from models.base import Base
engine = create_engine("sqlite:///teste.db", echo=True)



