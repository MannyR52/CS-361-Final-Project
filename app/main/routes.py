from flask import Blueprint
from flask import render_template, request, Blueprint
from app.models import Workout


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html")


@main.route("/about")
def about():
    return render_template("about.html", title="About")
