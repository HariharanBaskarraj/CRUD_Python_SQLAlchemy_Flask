from pydantic import BaseModel


class CreateJobRequest(BaseModel):
    projectname: str
    description: str
    metadatamodelname: str
    selectedcategory: int
    selectedfield: int
    selectedmodel: int
