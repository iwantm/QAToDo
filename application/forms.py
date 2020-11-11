from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Todos


class CheckIfExists:
    def __init__(self, message=None):
        self.todos = Todos.query.all()
        if not message:
            message = 'Already Exists'
        self.message = message

    def __call__(self, form, field):
        for todo in self.todos:
            if field.data.lower().replace(" ", "") == todo.name.lower().replace(" ", ""):
                raise ValidationError(self.message)


class TodoForm(FlaskForm):
    name = StringField(u'Name', validators=[
        DataRequired(),
        CheckIfExists(),
        Length(min=5, max=50)
    ])
    submit = SubmitField('Add Todo')


class OrderingForm(FlaskForm):
    order = SelectField('Order: ', choices=[
        ("completed", "Completed"),
        ("new", "Newest"),
        ("old", "Oldest"),
        ("incomplete", "Not Complete")
    ])
    submit = SubmitField('Order')
