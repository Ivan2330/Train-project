from sqlalchemy import Column, Enum, String, Integer, ForeignKey, DateTime, UUID
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
import enum

Base = declarative_base()


class UserStatus(enum.Enum):
    COMPANY_OWNER = "company_owner"
    LEADER_OF_PROJECT = "leader_of_project"
    PROJECT_DIRECTOR = "projects_director"
    SIMPLE_USER = "simple_user"


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user_table"

    # project_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    user_status = Column(Enum(UserStatus), nullable=False)
    
    projects = relationship("Project", back_populates="owner")
    tasks = relationship("Task", back_populates="assignee")


class ProjectProcessStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class ProjectPriority(enum.Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Project(Base):
    __tablename__ = "projects_info"
    
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String, unique=True)
    project_status = Column(Enum(ProjectProcessStatus), nullable=False)
    project_priority = Column(Enum(ProjectPriority), nullable=False)
    owner_id = Column(UUID, ForeignKey("user_table.id"))

    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")


class Task(Base):
    __tablename__ = "tasks"
    
    task_id = Column(Integer, primary_key=True)
    task_name = Column(String, unique=True)
    project_id = Column(Integer, ForeignKey("projects_info.project_id"))
    assignee_id = Column(UUID, ForeignKey("user_table.id"))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User", back_populates="tasks")