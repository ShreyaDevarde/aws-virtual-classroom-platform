"""
Authentication Routes
"""

from flask import (Blueprint,render_template,request,redirect,url_for,flash,session)
from werkzeug.security import (generate_password_hash,check_password_hash)
from models.user import User


auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/")
def home():
    return render_template("home.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["email"]
        password = request.form["password"]


        existing_user = User.get_user_by_username(
            username
        )

        if existing_user:
            flash(
                "User already exists",
                "danger"
            )
            return redirect(
                url_for("auth.register")
            )

        hashed_password = generate_password_hash(
            password
        )

        User.create_user(
            username,
            hashed_password
        )

        flash(
            "Registration successful",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html"
    )


# @auth_bp.route("/login", methods=["GET", "POST"])
# def login():

#     if request.method == "POST":

#         username = request.form["username"]
#         password = request.form["password"]

#         user = User.get_user_by_username(
#             username
#         )

#         if (
#             user
#             and
#             check_password_hash(
#                 user["password"],
#                 password
#             )
#         ):

#             session["username"] = username

#             flash(
#                 "Login successful",
#                 "success"
#             )

#             return redirect(
#                 url_for(
#                     "content.content"
#                 )
#             )

#         flash(
#             "Invalid credentials",
#             "danger"
#         )

#     return render_template(
#         "login.html"
#     )
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if (
            username == "admin@test.com"
            and
            password == "admin123"
        ):

            session["username"] = username

            return redirect(
                url_for("content.content")
            )

        flash(
            "Invalid Credentials",
            "danger"
        )

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged out successfully",
        "info"
    )

    return redirect(
        url_for("auth.home")
    )