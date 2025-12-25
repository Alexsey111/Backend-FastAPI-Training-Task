from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_url():
    response = client.post("/", json={"url": "https://example.com"})
    assert response.status_code == 201
    assert "short_id" in response.json()


def test_redirect_url():
    post_response = client.post("/", json={"url": "https://example.com"})
    short_id = post_response.json()["short_id"]

    get_response = client.get(f"/{short_id}", follow_redirects=False)
    assert get_response.status_code == 307

    # Приводим к базовому URL без слэша в конце
    assert get_response.headers["location"].rstrip("/") == "https://example.com"


def test_redirect_not_found():
    response = client.get("/nonexistent", follow_redirects=False)
    assert response.status_code == 404
