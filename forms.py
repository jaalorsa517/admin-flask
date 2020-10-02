from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FormField, FieldList, SelectField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    nickname = StringField(label='Nickname', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField()


class RowForm(FlaskForm):
    nickname = StringField(label='Nickname', validators=[DataRequired()])
    check = BooleanField('admin')


class TableForm(FlaskForm):
    rows = FieldList(FormField(RowForm))
    submit = SubmitField()
