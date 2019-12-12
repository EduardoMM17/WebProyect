from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(message='Ingresa tu nombre de usuario')])
    password = PasswordField('Contrasenia', validators=[DataRequired('Ingresa una contra porfavor!')])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Ingresar')

