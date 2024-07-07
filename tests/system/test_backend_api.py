import pytest
from fastapi.testclient import TestClient

from oi.ai.mleng.takehome.backend.api import app

client = TestClient(app)


@pytest.mark.parametrize(
    "url, status",
    [
        (
            (
                "https://cdn.mos.cms.futurecdn.net/"
                "WNDjvbcKm6GfW5qYhZdJQV-1200-80.jpg"
            ),
            200,
        ),
    ],
)
def test_prediction_service(url, status):
    response = client.post(
        "/predict",
        data={"url": url},
    )
    assert response.status_code == status
