from flask import Blueprint
from flask import render_template, request, Blueprint
import json
import random


gen_random = Blueprint('random', __name__)


@gen_random.route('/random', methods=['GET', 'POST'])

def rand_val():
    exer = ''
    if request.method == "POST":
        with open('app/exercises.json') as f:
            data = json.load(f)
        val = random.randint(0, 7)

        exer = data['exercises'][val]

    return render_template("random.html", title="Random Exercise", exer=exer)


