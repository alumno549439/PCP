from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MusicaForm(FlaskForm):
    artista = StringField('Artista / Banda', validators=[DataRequired()])
    album = StringField('Álbum', validators=[DataRequired()])
    genero = StringField('Género musical', validators=[DataRequired()])
    submit = SubmitField('Guardar Disco')