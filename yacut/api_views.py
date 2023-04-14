from flask import jsonify, request

from settings import API_ADD_URL, API_GET_URL, SHORT_LINK, URL
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from . import app


@app.route(API_GET_URL, methods=['GET'])
def get_url(short_id):
    """Возвращает оригинальную ссылку по указанному short_id"""
    urlmap = URLMap.check_custom_id_exists(short_id)
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({URL: urlmap.original}), 200


@app.route(API_ADD_URL, methods=['POST'])
def add_url():
    """Создает короткую ссылку на указанный URL-адрес"""
    data = request.get_json()
    data = URLMap.validate_api_fields(data)
    URLMap.save_to_db(data)
    return jsonify({
        URL: data[URL],
        SHORT_LINK: data[SHORT_LINK],
    }), 201
