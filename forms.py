from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import __init__


class RegistrationForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    verified_password = PasswordField("Repeat password", [
        EqualTo('password', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Register')

    def check_email(self, email):
        user = __init__.User.query.filter_by(
            email=email.data).first()
        if user:
            raise ValidationError(
                'This email is used. Choose another.')


class LoginForm(FlaskForm):
    email = StringField(
        'Email', [DataRequired()])
    password = PasswordField(
        'Password', [Length(min=5), DataRequired()])
    submit = SubmitField('Login')


class AddBillForma(FlaskForm):
    amount = StringField('Amount', [DataRequired()])
    description = StringField('Description', [DataRequired()])
    submit = SubmitField('Add')


class AddGroupForma(FlaskForm):
    group_id = StringField('Group ID', [DataRequired()])
    submit = SubmitField('Add')
