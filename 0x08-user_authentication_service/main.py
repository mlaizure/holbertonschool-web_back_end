#!/usr/bin/env python3
"""
End-to-end integration test module
"""
import requests
from app import AUTH


def register_user(email: str, password: str) -> None:
    """registers new user with email and password"""
    payload = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/users', payload)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """tries to log in user with email and incorrect password"""
    payload = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/sessions', payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """logs in user with correct email and password"""
    payload = {'email': email, 'password': password}
    response = requests.post('http://localhost:5000/sessions', payload)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'logged in'}
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """testing profile route with invalid session id"""
    response = requests.get('http://127.0.0.1:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """testing profile route with valid session id"""
    cookies = {'session_id': session_id}
    response = requests.get('http://127.0.0.1:5000/profile', cookies)
    user = AUTH.get_user_from_session_id(session_id)
    assert response.status_code == 200
    assert response.json() == {'email': user.email}


def log_out(session_id: str) -> None:
    """testing logging out a user"""
    cookies = {'session_id': session_id}
    response = requests.delete('http://127.0.0.1:5000/sessions', cookies)
    assert response.status_code == 200
    assert response.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    """testing password reset token creation"""
    payload = {'email': email}
    response = requests.post('http://127.0.0.1:5000/reset_password', payload)
    user = AUTH._db.find_user_by(email=email)
    assert response.status_code == 200
    assert response.json() == {'email': email,
                               'reset_token': user.reset_token}
    return user.reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """testing password updating functionality"""
    payload = {'email': email, 'reset_token': reset_token,
               'new_password': new_password}
    response = request.put('http://127.0.0.1:5000/reset_password', payload)
    assert response.status_code == 200
    assert response.json() == {'email': email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
