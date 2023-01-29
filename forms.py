from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import __init__


class RegistracijosForma(FlaskForm):
    vardas = StringField('Name', [DataRequired()])
    el_pastas = StringField('Email', [DataRequired(), Email()])
    slaptazodis = PasswordField('Password', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField("Repeat password", [
                                             EqualTo('slaptazodis', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Register')

    def check_email(self, el_pastas):
        vartotojas = __init__.Vartotojas.query.filter_by(
            el_pastas=el_pastas.data).first()
        if vartotojas:
            raise ValidationError(
                'This email is used. Choose another.')


class PrisijungimoForma(FlaskForm):
    el_pastas = StringField(
        'Email', [DataRequired()])
    slaptazodis = PasswordField(
        'Password', [Length(min=5), DataRequired()])
    submit = SubmitField('Login')


class AddBillForma(FlaskForm):
    amount = StringField('Amount', [DataRequired()])
    description = StringField('Description', [DataRequired()])
    submit = SubmitField('Add')


class AddGroupForma(FlaskForm):
    group_id = StringField('Group ID', [DataRequired()])
    submit = SubmitField('Add')
