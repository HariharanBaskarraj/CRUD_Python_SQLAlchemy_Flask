from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from .database import base
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()

# class Employee(base):
#     __tablename__ = 'employees'
#
#     id = Column(Integer , primary_key=True)
#     name = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)
#     city = Column(String, nullable=False)



class Category(base):
    __tablename__ = 'category'

    category_id = Column(Integer(), primary_key=True)
    category_name = Column(String(), nullable=False)
    category_value = Column(Integer(), nullable=False)
    category_ref = Column(String(), nullable=False)
    field = relationship('Field')


#     fields = relationship('Field', backref='Field.field_id',primaryjoin='Category.category_id==Field.field_id', lazy='dynamic')

class Field(base):
   __tablename__ = 'field'

   field_id = Column(Integer, primary_key=True)
   field_name = Column(String, nullable=False)
   field_ref = Column(String, nullable=False)
   type_name = Column(String, nullable=False)
   category_id = Column(Integer(),ForeignKey('category.category_id'))


class Model(base):
   __tablename__ = 'model'

   model_id = Column(Integer, primary_key=True)
   model_name = Column(String, nullable=False)
   model_str = Column(String, nullable=False)

class Project(base):
    __tablename__ = 'aiproject'

    project_id = Column(Integer, primary_key=True)
    projectname = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    metadatamodelname = Column(String(255), nullable=False)
    selectedcategory =  Column(Integer(),ForeignKey('category.category_id'))
    selectedfield = Column(Integer(), ForeignKey('field.field_id'))
    selectedmodel = Column(Integer(), ForeignKey('model.model_id'))


# class Field(base):
#     __tablename__ = 'field'
#
#     field_id = Column(Integer, primary_key=True)
#     category_id = Column(Integer, ForeignKey('category.category_id'), nullable=False)
#     field_name = Column(String, nullable=False)
#     field_ref = Column(String, nullable=False)
#     type = Column(String, nullable=False)
#
#     category = relationship("Category", back_populates="fields")
