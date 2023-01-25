from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import __init__


# def group_query():
#     return __init__.Group.query


class RegistracijosForma(FlaskForm):
    vardas = StringField('Name', [DataRequired()])
    el_pastas = StringField('Email', [DataRequired()])
    slaptazodis = PasswordField('Password', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField("Repeat password", [
                                             EqualTo('slaptazodis', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Register')

    def tikrinti_varda(self, vardas):
        vartotojas = __init__.Vartotojas.query.filter_by(
            vardas=vardas.data).first()
        if vartotojas:
            raise ValidationError('Šis vardas panaudotas. Pasirinkite kitą.')

    def tikrinti_pasta(self, el_pastas):
        vartotojas = __init__.Vartotojas.query.filter_by(
            el_pastas=el_pastas.data).first()
        if vartotojas:
            raise ValidationError(
                'Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class PrisijungimoForma(FlaskForm):
    el_pastas = StringField('Email', [DataRequired()])
    slaptazodis = PasswordField('Password', [DataRequired()])
    prisiminti = BooleanField("Remember me")
    submit = SubmitField('Login')


class AddBillForma(FlaskForm):
    amount = StringField('Amount', [DataRequired()])
    description = StringField('Description', [DataRequired()])
    submit = SubmitField('Add')


# class AddGroupForma(FlaskForm):
#     group_id = StringField('Group_ID', [DataRequired()])
#     group = QuerySelectField(query_factory=group_query, allow_blank=True,
#                              get_label="Name", get_pk=lambda obj: str(obj))
#     submit = SubmitField('Add')
