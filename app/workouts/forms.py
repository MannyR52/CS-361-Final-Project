from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired


class WorkoutForm(FlaskForm):
    name = StringField('Workout Name', validators=[DataRequired()])
    weight = StringField('Weight(lb)', validators=[DataRequired()])
    repetitions = StringField('Repetitions', validators=[DataRequired()])
    sets = StringField('Sets', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Enter in log')


