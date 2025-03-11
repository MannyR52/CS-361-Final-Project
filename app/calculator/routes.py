from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Workout
from app.calculator.forms import CalculatorForm


calculator = Blueprint("calculator", __name__)


@calculator.route("/calculator", methods=['GET', 'POST'])
def bmi():
    form = CalculatorForm()
    bmi_val = ""
    if request.method == 'POST':
        w = float(request.form.get('weight'))
        h = float(request.form.get('height'))
        bmi_val = (w/(h ** 2)) * 703
        bmi_val = int(round(bmi_val, 2))
    return render_template("calc.html", title="BMI Calculator", form=form, bmi_val=bmi_val)
