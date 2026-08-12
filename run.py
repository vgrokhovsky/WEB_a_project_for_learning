# from config import Config as user_config
from flask import Flask, render_template, request

from app.db_func.models import db
from app.users.routes import users_bp
from app.users.test import test

app = Flask(__name__)
# app.config.from_object(user_config)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    user_name = ""

    if request.method == "POST":
        user_name = request.form["text"]

    item_list = ["Bob", "Alex", "Foo"]
    return render_template(
        "index.html", user_name=user_name, item_list=item_list
    )


app.register_blueprint(users_bp, url_prefix="/users")


if __name__ == "__main__":
    app.run(debug=True)
