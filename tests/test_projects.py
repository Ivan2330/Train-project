import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_project():
    login_response = client.post("/auth/jwt/login", data={
        "username": "testuser@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]

    response = client.post("/projects/", json={
        "project_name": "Test Project",
        "project_status": "IN_PROGRESS",
        "project_priority": "HIGH"
    }, headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert response.json()["project_name"] == "Test Project"

@pytest.mark.asyncio
async def test_get_project():
    login_response = client.post("/auth/jwt/login", data={
        "username": "testuser@example.com",
        "password": "testpassword123"
    })
    token = login_response.json()["access_token"]

    response = client.get("/projects/1", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert response.json()["project_name"] == "Test Project"
