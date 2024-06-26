#!/usr/bin/env python3
""" Task 6 - Basic Flask App """

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def hello():
    """ Task 6 - Returns a welcome message """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """ Task 7 - Creates User """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH._db.find_user_by(email=email)
        return jsonify({"message": "email already registered"}), 400
    except NoResultFound:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """ Task 11 - Login """
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        message = jsonify({"email": email, "message": "logged in"})
        message.set_cookie("session_id", session_id)
        return message
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """ Task 14 - Logout """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for("hello"))
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """ Task 15 - Profile """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": f"{user.email}"}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """ Task 17 - Get Password Reset Token """
    email = request.form.get("email")

    try:
        user = AUTH._db.find_user_by(email=email)
    except NoResultFound:
        abort(403)

    reset_token = AUTH.get_reset_password_token(email)
    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route("/update_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """ Task 19 - Updates Password """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    if not email or not reset_token or not new_password:
        abort(400)

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
