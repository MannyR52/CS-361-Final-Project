from flask import Blueprint
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Workout
from app.workouts.forms import WorkoutForm

workouts = Blueprint('workouts', __name__)


@workouts.route("/log", methods=['GET', 'POST'])
@login_required
def log():
    workout = Workout.query.all()
    return render_template("log.html", title="Workout Log", workout=workout)


@workouts.route("/log/new", methods=['GET', 'POST'])
@login_required
def new_log():
    form = WorkoutForm()
    if form.validate_on_submit():
        workout = Workout(name=form.name.data, date=form.date.data, weight=form.weight.data,
                          repetitions=form.repetitions.data, sets=form.sets.data)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been logged.', 'success')
        return redirect(url_for('workouts.log'))
    return render_template('create_workout.html', title='Add Workout', form=form,
                           legend='Add Workout')


@workouts.route("/log/<int:workout_id>")
def workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    return render_template('workout.html', title=workout.name, workout=workout)


@workouts.route("/log/<int:workout_id>/update", methods=['GET', 'POST'])
@login_required
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    form = WorkoutForm()
    if form.validate_on_submit():
        workout.name = form.name.data
        workout.date = form.date.data
        workout.weight = form.weight.data
        workout.repetitions = form.repetitions.data
        workout.sets = form.sets.data
        db.session.commit()
        flash('Your workout has been updated.', 'success')
        return redirect(url_for('workouts.log', workout_id=workout.id))
    elif request.method == 'GET':
        form.name.data = workout.name
        form.date.data = workout.date
        form.weight.data = workout.weight
        form.repetitions.data = workout.repetitions
        form.sets.data = workout.sets
    return render_template('create_workout.html', title='Update Workout', form=form,
                           legend='Update Workout')


@workouts.route("/log/<int:workout_id>/delete", methods=['POST'])
@login_required
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Your workout has been deleted!', 'success')
    return redirect(url_for('workouts.log'))

