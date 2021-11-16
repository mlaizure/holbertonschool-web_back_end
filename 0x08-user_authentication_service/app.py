#!/usr/bin/env python3
"""
Route module for the user auth service
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', methods=['GET'])
def hello_world():
    """returns json"""
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """registers user and returns jsonified info or 400 if user
    already registered"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify(email=email, message='user created')
    except ValueError:
        return jsonify(message='email already registered'), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """creates session for user"""
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify(email=email, message='logged in')
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """find user with session id, destroy session and redirect user to GET"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """find user with session id, respond with 200 and email jsonified"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify(email=user.email), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """generate a token and respond with email and reset token"""
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify(email=email, reset_token=reset_token), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """update a user's pssword"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, password)
    except ValueError:
        abort(403)
    return jsonify(email=email, message='Password updated')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
