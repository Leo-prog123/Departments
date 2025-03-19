from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    title = StringField('Название департамента', validators=[DataRequired()])
    chief = IntegerField('Шеф', validators=[DataRequired()])
    members = StringField('Участники', validators=[DataRequired()])
    email = EmailField('Почта департамента', validators=[DataRequired()])
    submit = SubmitField('Добавить')
