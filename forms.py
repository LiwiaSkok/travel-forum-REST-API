from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Optional
from wtforms import SelectField
from wtforms import SubmitField


class PostForm(FlaskForm):
    title = StringField("Tytuł", validators=[DataRequired()])
    content = TextAreaField("Treść", validators=[DataRequired()])
    location = StringField("Miejsce", validators=[Optional()])
    image = FileField("Zdjęcie", validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image2 = FileField("Drugie zdjęcie", validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg'])])
    country = SelectField("Kraj", choices=[
        ('Francja', 'Francja'),
        ('Wlochy', 'Włochy'),
        ('Hiszpania', 'Hiszpania'),
        ('Polska', 'Polska'),
        ('Chorwacja', 'Chorwacja'),
        ('Grecja', 'Grecja'),
        ('Niemcy', 'Niemcy')
    ], validators=[Optional()])
    submit = SubmitField("Dodaj post")

image = FileField("Zdjęcie (JPG, PNG)", validators=[
    FileAllowed(['jpg', 'jpeg', 'png'], 'Tylko pliki JPG, PNG!')
])
image2 = FileField("Drugie zdjęcie (opcjonalnie)", validators=[
    FileAllowed(['jpg', 'jpeg', 'png'], 'Tylko pliki JPG, PNG!')
])

class CommentForm(FlaskForm):
    content = TextAreaField("Treść komentarza", validators=[DataRequired()])
    submit = SubmitField("Dodaj komentarz")

from wtforms import SelectField

