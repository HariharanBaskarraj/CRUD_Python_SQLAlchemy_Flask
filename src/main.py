from fastapi import FastAPI, Depends, HTTPException, Header
from keycloak import KeycloakOpenID
from sqlalchemy.orm import Session
from .schemas import CreateJobRequest
from .database import get_database
from .models import Employee

app = FastAPI()

KEYCLOAK_SERVER_URL = "http://192.168.1.20:18080/auth"
REALM_NAME = "AI-Product"
CLIENT_ID = "AI-Product"

keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_SERVER_URL, realm_name=REALM_NAME, client_id=CLIENT_ID)

# Dependency to get the OAuth2 token from the request headers
def get_token(authorization: str = Header(...)):
    try:
        token = authorization.split("Bearer ")[1]
    except IndexError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

# Dependency to authenticate using Keycloak
def authenticate_token(token: str = Depends(get_token)):
     try:
        keycloak_openid.introspect(token)
        yield
     except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/")
def get_all(db: Session = Depends(get_database), token: str = Depends(authenticate_token)):
    return db.query(Employee).all()

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


# @app.get("/")
# def get_all(db: Session = Depends(get_database)):
#     return db.query(Employee).all()


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
