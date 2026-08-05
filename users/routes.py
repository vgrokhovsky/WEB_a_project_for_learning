from flask import Blueprint, jsonify, redirect, render_template, request

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
    template_folder="templates",
)


@users_bp.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"module": "users", "status": "ok"})


@users_bp.route("/profile", methods=["GET"])
def profile():
    data = {
        "user_name": "Bob",
    }
    return render_template("users/profile.html", data=data)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            # db fun
            redirect()
    return render_template("users/register.html")
