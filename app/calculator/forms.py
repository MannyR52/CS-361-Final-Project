from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CalculatorForm(FlaskForm):
    weight = StringField('Weight in pounds', validators=[DataRequired()])
    height = StringField('Height in inches', validators=[DataRequired()])
    submit = SubmitField('Calculate')
