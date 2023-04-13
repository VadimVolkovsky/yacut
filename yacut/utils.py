
import random
import string

from yacut.models import URLMap


def check_custom_id_exists(custom_id):
    """Проверяет существование аналогичного custom_id в БД"""
    custom_id = URLMap.query.filter_by(short=custom_id).first()
    if custom_id is not None:
        return custom_id
    return None


def generate_custom_id(letter_count=3, digit_count=3):
    """Генерирурет строку из заданного количества символов"""
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
    letters_and_digits = list(str1)
    random.shuffle(letters_and_digits)
    custom_id = ''.join(letters_and_digits)
    while check_custom_id_exists(custom_id) is not None:
        custom_id = generate_custom_id()
    return custom_id


def create_short_link(custom_id=None):
    """Создает короткую ссылку"""
    main_url = 'http://localhost/'
    if custom_id is None:
        custom_id = generate_custom_id()
    short = main_url + custom_id
    return short, custom_id