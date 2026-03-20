import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture(scope="module")
def response():
    res = requests.get(BASE_URL)
    return res


def test_status_code(response):
    assert response.status_code == 200


def test_response_structure(response):
    data = response.json()
    required_keys = {"userId", "id", "title", "body"}

    for post in data:
        assert required_keys.issubset(post.keys())


def test_save_first_5_posts(response):
    data = response.json()
    first_five = data[:5]

    import json
    with open("first_5_posts.json", "w") as file:
        json.dump(first_five, file, indent=4)

    assert len(first_five) == 5