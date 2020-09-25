from admin import app
from apps.auth import auth

def test_index():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_login():
    response = app.test_client().get('/auth/login')
    assert response.status_code == 200


def test_singup():
    response = app.test_client().get('/auth/singup')
    assert response.status_code == 200
