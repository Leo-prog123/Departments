from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class RegisterJobForm(FlaskForm):
    job = StringField('Описание работы', validators=[DataRequired()])
    team_leader = IntegerField('Руководитель', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    work_size = IntegerField('Объем работы', validators=[DataRequired()])
    is_finished = BooleanField('Pабота окончена', validators=[DataRequired()])
    submit = SubmitField('Добавить')
