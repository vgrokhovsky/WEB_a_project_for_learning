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
            redirect(url_for("users.profile"))
    return render_template("users/register.html")


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email and password:
            # db fun
            redirect(url_for("users.profile"))
    return render_template("users/login.html")


@users_bp.route("/logout", methods=["GET"])
def logout():
    # db fun
    return redirect(url_for("users.login"))
