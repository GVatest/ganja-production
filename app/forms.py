from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Massage', validators=[DataRequired()])
    send = SubmitField('Send')


class ReviewForm(FlaskForm):
    rname = StringField('Name', validators=[DataRequired()])
    remail = StringField('Email', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    leave = SubmitField('Leave')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    login = SubmitField('Login')


class UploadForm(FlaskForm):
    path_to_folder = StringField('path_to_folder')