from fastapi import FastAPI, Depends, HTTPException, Header
from keycloak import KeycloakOpenID
from sqlalchemy.orm import Session
from .schemas import CreateJobRequest
from .database import get_database
# from .models import Employee
from .models import Category
from .models import Field
from .models import Model
from .models import Project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origin or origins for your Angular app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/categories")
def get_categories(db: Session = Depends(get_database)):
    return db.query(Category).all()

@app.get("/fields/{category_id}")
def get_fields_by_category_id(category_id: int, db: Session = Depends(get_database)):
    category = db.query(Category).filter(Category.category_id == category_id).first()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return db.query(Field).filter(Field.category_id == category_id).all()


@app.get("/models")
def get_models(db: Session = Depends(get_database)):
    return db.query(Model).all()


@app.post("/create")
def create(details: CreateJobRequest, db: Session = Depends(get_database)):
    to_create = Project(

        projectname=details.projectname,
        description=details.description,
        metadatamodelname=details.metadatamodelname,
        selectedcategory=details.selectedcategory,
        selectedfield=details.selectedfield,
        selectedmodel=details.selectedmodel
    )

    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

# @app.post("/")
# def create(details: CreateJobRequest, db: Session = Depends(get_database)):
#     to_create = Employee(
#         name=details.name,
#         age=details.age,
#         city=details.city
#     )
#
#     db.add(to_create)
#     db.commit()
#     return {
#         "success": True,
#         "created_id": to_create.id
#     }
#
#
# @app.get("/{id}")
# def get_by_id(id: int, db: Session = Depends(get_database)):
#     return db.query(Employee).filter(Employee.id == id).first()
#
#
#
#
#
# @app.delete("/{id}")
# def delete_by_id(id: int, db: Session = Depends(get_database)):
#     db.query(Employee).filter(Employee.id == id).delete()
#     db.commit()
#     return {
#         "success": True
#     }
#
#
# @app.delete("/")
# def delete_by_id(db: Session = Depends(get_database)):
#     db.query(Category).delete()
#     db.commit()
#     return {
#         "success": True
#     }
#
#
# @app.put("/{id}")
# def update_employee(id: int, updated_data: dict, db: Session = Depends(get_database)):
#     existing_employee = db.query(Employee).filter(Employee.id == id).first()
#
#     if not existing_employee:
#         raise HTTPException(status_code=404, detail="Employee not found")
#
#     for key, value in updated_data.items():
#         setattr(existing_employee, key, value)
#
#     db.commit()
#     return {
#         "message": "Employee updated successfully"
#     }
