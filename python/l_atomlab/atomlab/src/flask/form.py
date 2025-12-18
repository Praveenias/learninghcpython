from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length



class TokenForm(FlaskForm):
    api_key = StringField('API-Key', validators=[DataRequired()])
    submit = SubmitField('Submit')

