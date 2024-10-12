from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import get_async_session
from app.models import Project 
from app.schemas import ProjectCreate, ProjectRead, ProjectUpdate
from app.auth import current_active_user


router = APIRouter()

@router.post("/", response_model=ProjectRead, tags=["projects"])
async def create_project(
    project: ProjectCreate, 
    session: AsyncSession = Depends(get_async_session),
    current_user = Depends(current_active_user),  # Поточний користувач
):
    new_project = Project(
        **project.model_dump(), 
        owner_id=current_user.id  # Встановлюємо поточного користувача як власника проекту
    )
    session.add(new_project)
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.get("/{project_id}", response_model=ProjectRead, tags=["projects"])
async def get_project(project_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Project).filter_by(project_id=project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.patch("/{project_id}", response_model=ProjectRead, tags=["projects"])
async def update_project(
    project_id: int,
    project: ProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(select(Project).filter_by(project_id=project_id))
    db_project = result.scalar_one_or_none()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in project.model_dump(exclude_unset=True).items():
        setattr(db_project, key, value)
    
    await session.commit()
    await session.refresh(db_project)
    return db_project


@router.delete("/{project_id}", tags=["projects"])
async def delete_project(project_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Project).filter_by(project_id=project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    await session.delete(project)
    await session.commit()
    return {"detail": "Project deleted successfully"}