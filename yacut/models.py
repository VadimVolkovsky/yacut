import uuid
from datetime import datetime

from settings import (CUSTOM_ID, CUSTOM_ID_MAX_GENERATED_LENGTH,
                      CUSTOM_ID_PATTERN, MAIN_URL, ORIGINAL, SHORT, SHORT_LINK,
                      URL)
from yacut.error_handlers import InvalidAPIUsage
from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(), nullable=False)
    short = db.Column(db.String(), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        """Десириализация данных: добавление в пустой объект класса URLMap
        значения полей, которые были получены в POST-запросе"""
        fields = {
            URL: ORIGINAL,
            CUSTOM_ID: SHORT
        }
        for field in [URL, CUSTOM_ID]:
            if field in data:
                field_name = fields[field]
                setattr(self, field_name, data[field])

    @staticmethod
    def create_short_link(custom_id):
        """Создает короткую ссылку"""
        short_link = MAIN_URL + custom_id
        return short_link

    @staticmethod
    def generate_custom_id():
        """Генерирурет случайную строку"""
        custom_id = str(uuid.uuid4())[:CUSTOM_ID_MAX_GENERATED_LENGTH]
        return custom_id

    @staticmethod
    def check_custom_id_exists(short_id):
        """Метод ищет и возвращает из БД объект URLMap по
        short_id(custom_id), если ничего не найдено вернется None"""
        urlmap = URLMap.query.filter_by(short=short_id).first()
        return urlmap

    @staticmethod
    def save_to_db(data):
        """Сохраняет новый объект в БД"""
        urlmap = URLMap()
        urlmap.from_dict(data)
        db.session.add(urlmap)
        db.session.commit()

    @staticmethod
    def validate_api_fields(data):
        """Валидация полей переданных через API"""
        if data is None:
            raise InvalidAPIUsage('Отсутствует тело запроса')
        if URL not in data:
            raise InvalidAPIUsage('"url" является обязательным полем!')
        if CUSTOM_ID in data:
            custom_id = URLMap.validate_custom_id(data[CUSTOM_ID])
        else:
            custom_id = URLMap.generate_custom_id()
        short_link = URLMap.create_short_link(custom_id)
        data[SHORT_LINK] = short_link
        data[CUSTOM_ID] = custom_id
        return data

    @staticmethod
    def validate_custom_id(custom_id):
        """Валидация поля custom_id"""
        if custom_id is None or len(custom_id) == 0:
            custom_id = URLMap.generate_custom_id()
        if not CUSTOM_ID_PATTERN.match(custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки', 400)
        if URLMap.check_custom_id_exists(custom_id):
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
        return custom_id
