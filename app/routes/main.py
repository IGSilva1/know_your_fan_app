from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db  # <-- novo import

import os
from ..utils.ocr import extract_text_from_image, validate_document_text
from ..social.twitter import fetch_twitter_data
from ..utils.profile_validator import validate_esports_profile

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/upload", methods=["POST"])
def upload():
    file = request.files["document"]
    ocr_result = None
    if file:
        filepath = os.path.join("app/static/uploads", file.filename)
        file.save(filepath)
        text = extract_text_from_image(filepath)
        result = validate_document_text(text)
        ocr_result = result
    return render_template("index.html", ocr_result=ocr_result)

@main.route("/social", methods=["POST"])
def social():
    username = request.form["username"]
    twitter_data = fetch_twitter_data(username)
    return render_template("index.html", twitter_data=twitter_data)
