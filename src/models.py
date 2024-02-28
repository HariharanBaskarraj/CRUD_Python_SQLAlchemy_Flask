from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import base


class Employee(base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String, nullable=False)
