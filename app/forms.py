from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[Length(min=4, max=25, 
                            message ='Це поле має бути довжиною між 4 та 25 символів'), 
                            DataRequired(message ="Це поле обов'язкове"),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                              'Username must have only '
                                              'letters, numbers, dots or '
                                              'underscores')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[Length(min=6, 
                            message ='Це поле має бути більше 6 cимволів'), 
                            DataRequired(message ="Це поле обов'язкове")])
    confirm_password = PasswordField('Confirm Password', 
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

            
class LoginForm(FlaskForm): 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')




'''


class Search(FlaskForm):
	search_text = StringField('Search for', validators=[DataRequired(message ='Це поле обовязкове')])
	submit = SubmitField('Search')

'''