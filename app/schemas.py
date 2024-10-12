import uuid
from datetime import datetime
from pydantic import BaseModel
from fastapi_users import schemas
from typing import Optional

class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str 
    user_status: str

    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    username: str | None = None
    user_status: str

    class Config:
        orm_mode = True

class UserUpdate(schemas.BaseUserUpdate):
    username: str | None = None
    user_status: str

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    project_name: str
    project_status: str
    project_priority: str
    
    class Config:
        orm_mode = True
    
class ProjectCreate(ProjectBase):
    pass

class ProjectRead(ProjectBase):
    project_id: int
    owner_id: uuid.UUID
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        orm_mode = True

class ProjectUpdate(BaseModel):
    project_name: str | None = None
    project_status: str | None = None
    project_priority: str | None = None
    owner_id: uuid.UUID | None = None

    class Config:
        orm_mode = True
        
class TaskBase(BaseModel):
    task_name: str
    project_id: int
    assignee_id: uuid.UUID | None = None

    class Config:
        orm_mode = True

class TaskCreate(TaskBase):
    pass
    
    class Config:
        orm_mode = True
        
class TaskRead(TaskBase):
    task_id: int
    created_at: datetime
    updated_at: datetime | None = None
    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    task_name: str | None = None
    project_id: int | None = None
    assignee_id: uuid.UUID | None = None

    class Config:
        orm_mode = True