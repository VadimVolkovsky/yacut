from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Optional


class UrlForm(FlaskForm):
    original = URLField(
        'Вставьте URL адресс',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = URLField(
        'Введите желаемую короткую ссылку',
        validators=[Optional()]
    )
    submit = SubmitField('Добавить')
