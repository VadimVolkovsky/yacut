from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Optional, Regexp

from settings import CUSTOM_ID_REGEX


class UrlForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
        ])
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Regexp(
                CUSTOM_ID_REGEX,
                message='Указано недопустимое имя для короткой ссылки')
        ])
    submit = SubmitField('Создать')
