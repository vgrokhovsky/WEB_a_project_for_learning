from flask import Blueprint, jsonify, redirect, render_template, request

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"module": "users", "status": "ok"})


@users_bp.route("/profile", methods=["GET"])
def profile():
    return render_template("users/profile.html")


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            # db fun
            redirect()
    return render_template("users/register.html")
