import pytest
from app import app, square_number


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Welcome to GitHub Actions CI/CD Deployment to EC2 Amazon Linux!" in res.data


def test_health_check(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json()['status'] == "healthy"


def test_square(client):
    res = client.get('/square/5')
    assert res.status_code == 200
    assert res.get_json()['square'] == 25


def test_square_function():
    assert square_number(4) == 16


def test_square_invalid_input():
    with pytest.raises(ValueError):
        square_number("not an integer")


def test_not_found(client):
    res = client.get('/nonexistent')
    assert res.status_code == 404
    assert b"Not Found" in res.data

# ✅ Add a blank line at the end
