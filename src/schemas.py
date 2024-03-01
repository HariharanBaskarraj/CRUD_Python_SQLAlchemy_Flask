from pydantic import BaseModel


class CreateJobRequest(BaseModel):
    name: str
    age: int
    city: str
