from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from app.db import User, get_db_and_tables
from app.schemas import UserCreate, UserRead, UserUpdate
from app.auth import auth_backend, current_active_user, fastapi_users
from app.tasks import router as tasks_router
from app.projects import router as projects_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    tasks_router, 
    prefix="/tasks", 
    tags=["tasks"],
    )
app.include_router(
    projects_router, 
    prefix="/projects", 
    tags=["projects"],
    )


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}