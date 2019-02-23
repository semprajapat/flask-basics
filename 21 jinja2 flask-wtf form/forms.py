from flask_wtf import Form
from wtforms import TextField,TextAreaField, IntegerField, SelectField,SubmitField,RadioField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField('name of student',[validators.Required('plz enter the name.')])
    Gender = RadioField('Gender',choices=[('M','male'),('F','female')])
    Address = TextAreaField('Address',[validators.Required('Enter the Address')])
    email = TextField('Email',[validators.Required('Enter the Email address'),validators.Email('plz enterthe Email')])
    Age = IntegerField('Age')
    Language = SelectField('Language',choices=[('cpp','c++'),('py','python')])
    Submit = SubmitField('send')

    