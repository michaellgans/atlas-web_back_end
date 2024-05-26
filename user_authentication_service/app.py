#!/usr/bin/env python3
""" Task 6 - Basic Flask App """

from flask import Flask, jsonify, request
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
        return jsonify({"email": email}, {"message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
