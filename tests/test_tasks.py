import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_task():
    login_response = client.post("/auth/jwt/login", data={
        "username": "testuser@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]

    
    response = client.post("/tasks/", json={
        "task_name": "Test Task",
        "project_id": 1
    }, headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert response.json()["task_name"] == "Test Task"

@pytest.mark.asyncio
async def test_get_task():
    login_response = client.post("/auth/jwt/login", data={
        "username": "testuser@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]

    response = client.get("/tasks/1", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert response.json()["task_name"] == "Test Task"
