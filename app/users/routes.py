from flask import (
    Blueprint,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
    template_folder="templates",
)
from app.db_func.user_func import create_user, get_user_by_id


@users_bp.route("/", methods=["GET", "POST"])
def index():
    return jsonify({"module": "users", "status": "ok"})


@users_bp.route("/profile/<id>", methods=["GET"])
def profile(id):

    user_obj = get_user_by_id(id)
    print(user_obj)
    data = {"user_email": user_obj.email}
    return render_template("users/profile.html", data=data)


@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            create_user(email=email, password=password)
            return redirect(url_for("users.login"))
    return render_template("users/register.html")


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            # db fun
            return redirect(url_for("users.profile"))
    return render_template("users/login.html")


@users_bp.route("/logout", methods=["GET"])
def logout():
    # db fun
    return redirect(url_for("users.login"))
