from fastapi import FastAPI, Depends, HTTPException
from .schemas import CreateJobRequest
from sqlalchemy.orm import Session
from .database import get_database
from .models import Employee

app = FastAPI()


@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_database)):
    to_create = Employee(
        name=details.name,
        age=details.age,
        city=details.city
    )

    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }


@app.get("/{id}")
def get_by_id(id: int, db: Session = Depends(get_database)):
    return db.query(Employee).filter(Employee.id == id).first()


@app.get("/")
def get_by_id(db: Session = Depends(get_database)):
    return db.query(Employee).all()


@app.delete("/{id}")
def delete_by_id(id: int, db: Session = Depends(get_database)):
    db.query(Employee).filter(Employee.id == id).delete()
    db.commit()
    return {
        "success": True
    }


@app.delete("/")
def delete_by_id(db: Session = Depends(get_database)):
    db.query(Employee).delete()
    db.commit()
    return {
        "success": True
    }


@app.put("/{id}")
def update_employee(id: int, updated_data: dict, db: Session = Depends(get_database)):
    existing_employee = db.query(Employee).filter(Employee.id == id).first()

    if not existing_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in updated_data.items():
        setattr(existing_employee, key, value)

    db.commit()
    return {
        "message": "Employee updated successfully"
    }
