"""
Content Routes
"""

from flask import (Blueprint,render_template,request,flash,redirect,url_for,session)
from services.s3_service import (upload_file,get_all_files)
from utils.validators import (is_allowed_file)

content_bp = Blueprint(
    "content",
    __name__
)

@content_bp.route(
    "/content",
    methods=["GET", "POST"]
)
def content():

    if "username" not in session:

        flash(
            "Please login first",
            "warning"
        )

        return redirect(
            url_for("auth.login")
        )

    if request.method == "POST":

        file = request.files.get("file")

        if not file:

            flash(
                "No file selected",
                "danger"
            )

            return redirect(
                url_for(
                    "content.content"
                )
            )

        if not is_allowed_file(
            file.filename
        ):

            flash(
                "Invalid file type",
                "danger"
            )

            return redirect(
                url_for(
                    "content.content"
                )
            )

        try:

            upload_file(file)

            flash(
                "File uploaded successfully",
                "success"
            )

        except Exception as e:

            flash(
                f"Upload failed: {e}",
                "danger"
            )

    courses = [
    {
        "id": 1,
        "name": "AWS Cloud Practitioner",
        "description": "Learn AWS fundamentals and cloud concepts.",
        "image": "images/aws.jpg"
    },
    {
        "id": 2,
        "name": "Python Programming",
        "description": "Master Python from beginner to advanced.",
        "image": "images/python.jpg"
    },
    {
        "id": 3,
        "name": "Machine Learning Basics",
        "description": "Introduction to Machine Learning concepts.",
        "image": "images/ml.jpg"
    }
]

    return render_template(
        "content.html",
        courses=courses
    )