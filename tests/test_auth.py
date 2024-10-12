import pytest
from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_register_user():
    response = client.post("/auth/register", json={
        "email": "testuser@example.com",
        "password": "testpassword123",
        "username": "testuser",
        "user_status": "SIMPLE_USER"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@example.com"

@pytest.mark.asyncio
async def test_login_user():
    response = client.post("/auth/jwt/login", data={
        "username": "testuser@example.com",
        "password": "testpassword123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
