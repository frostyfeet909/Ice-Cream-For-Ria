"""Test the index endpoint.

Provides:
- test_index: Test the index endpoint.
"""

from fastapi.testclient import TestClient

from api.router.endpoints.index import router as app

client = TestClient(app)


def test_index():
    """Test the index endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World!"}
