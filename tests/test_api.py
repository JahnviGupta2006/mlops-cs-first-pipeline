# Import TestClient so we can send simulated HTTP requests
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_health_endpoint(): # method ka naam test se start krna zruri hai
    """
    Verify that the application is running an can respond to a health-check request
    """

    response = client.get("/health")
    assert response.status_code == 200  # assertion error (just like if but checks if condition is true else return an error)
    assert response.json() == {"status" : "healthy"}

def test_valid_iris_prediction():
    """
    Verify that we are getting valid predictions
    """

    payload = {
    "sepal_length": 3.4,
    "sepal_width": 1.4,
    "petal_length": 3.4,
    "petal_width": 0.4
    }

    # send a simulated POST request with JSON input

    response = client.post("/predict", json = payload)

    # Endpoint should accept the valid request
    assert response.status_code == 200

    result = response.json()
    assert "prediction" in result
    assert "class_name" in result
    assert result["class_name"] in ["setosa", "versicolor", "virginica"]
    assert result["prediction"] in [0, 1, 2]