from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# login and registration


class SearchForm(FlaskForm):
    searched = StringField('Searched',
                         id='Searched',
                         validators=[DataRequired()])