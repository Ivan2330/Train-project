from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import get_async_session
from app.models import Task
from app.schemas import TaskCreate, TaskRead, TaskUpdate
from app.auth import current_active_user


router = APIRouter()


@router.post("/", response_model=TaskRead, tags=["tasks"])
async def create_task(
    task: TaskCreate,
    session: AsyncSession = Depends(get_async_session),
    current_user = Depends(current_active_user),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if not task.assignee_id:
        id=current_user.id
    else:
        id=task.assignee_id
    new_task = Task(
        task_name=task.task_name,
        project_id=task.project_id,
        assignee_id=id
    )
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task


@router.get("/{task_id}", response_model=TaskRead, tags=["tasks"])
async def get_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Task).filter_by(task_id=task_id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}", response_model=TaskRead, tags=["tasks"])
async def update_task(
    task_id: int,
    task: TaskUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    result = await session.execute(select(Task).filter_by(task_id=task_id))
    db_task = result.scalar_one_or_none()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
    
    await session.commit()
    await session.refresh(db_task)
    return db_task


@router.delete("/{task_id}", tags=["tasks"])
async def delete_task(task_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Task).filter_by(task_id=task_id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    await session.delete(task)
    await session.commit()
    return {"detail": "Task deleted successfully"}
