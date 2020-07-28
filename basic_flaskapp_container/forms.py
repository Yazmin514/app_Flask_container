from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
    name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre Incorrecto")])
    apellidos = StringField('Apellidos', validators=[DataRequired(), Length(min=4, max=50, message="Apellidos Incorrectos")])
    biografia = StringField('Descripcion', validators=[DataRequired(), Length(min=3, max=50, message="Descripcion Incorrecta")])
    correo = StringField('Email', validators=[DataRequired(), Length(min=3, max=50, message="Correo Incorrecto")])
    telefono = StringField('Telefono', validators=[DataRequired(), Length(min=3, max=50, message="Telefono Incorrecto")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=50, message="Contraseña Incorrecta")])

class LoginFrom(FlaskForm):
    name = StringField('User name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre Incorrecto")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20, message="Contraseña Incorrecto")])


class Fpublicacion(FlaskForm):
    publicacion = TextAreaField('Crear publicacion', validators=[Length(min=5, max=200)])