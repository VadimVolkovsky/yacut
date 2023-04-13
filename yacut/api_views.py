import re

from flask import jsonify, request

from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import check_custom_id_exists, create_short_link

from . import app, db

pattern = re.compile('^[a-zA-Z0-9]{1,16}$')


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    short_url = URLMap.query.filter_by(short=short_id).first()
    if short_url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': short_url.original}), 200


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' in data:
        custom_id = data['custom_id']

        if custom_id is None or len(custom_id) == 0:
            short_link, custom_id = create_short_link()
            data['custom_id'] = custom_id

        if not pattern.match(custom_id):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки', 400)

        if check_custom_id_exists(custom_id):
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')

        short_link, custom_id = create_short_link(custom_id)
        data['custom_id'] = custom_id
    else:
        short_link, custom_id = create_short_link()
        data['custom_id'] = custom_id

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({'url': data['url'], 'short_link': short_link, }), 201
