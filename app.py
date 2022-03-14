from fastapi import FastAPI
#import these three things
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime

app = FastAPI()
frameworkdb = []
# student model
class Framework(BaseModel):
    id: int
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    is_active: Optional[bool] = False

@app.get("/framework")
def read_framework_list():
    return frameworkdb

@app.post("/framework")
def create_framework(framework:Framework):
    frameworkdb.append(framework.dict())
    return frameworkdb[-1]

@app.get("/framework/{framework_id}")
def read_framework(framework_id: int):
    return frameworkdb[framework_id]

@app.put("/framework/{framework_id}")
def update_framework(framework_id: int,framework:Framework):
    frameworkdb[framework_id] = framework
    return frameworkdb[framework_id]

@app.delete("/framework/{framework_id}")
def delete_framework(framework_id: int):
    return frameworkdb.pop(framework_id)


