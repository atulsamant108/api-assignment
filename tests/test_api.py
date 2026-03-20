import requests
import pytest
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"

# JSON Schema for posts
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
    "required": ["userId", "id", "title", "body"]
}


# 1. Response Time Test
def test_response_time():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.elapsed.total_seconds() < 2


# 2. Schema Validation Test
def test_schema_validation():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()

    for post in data:
        validate(instance=post, schema=post_schema)


# 3. Parameterized Test
@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/users"
])
def test_multiple_endpoints(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")

    # status check
    assert response.status_code == 200

    # basic response validation
    assert isinstance(response.json(), list)