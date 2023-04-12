from . import app, db
from flask import redirect, render_template, url_for
from short_links_app.forms import UrlForm
from short_links_app.models import URLMap

import random  
import string  


def generate_custom_id(letter_count=3, digit_count=3): 
    """Генерирурет строку из заданного количества символов""" 
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
  
    letters_and_digits = list(str1)
    random.shuffle(letters_and_digits)  
    custom_id = ''.join(letters_and_digits)
    return custom_id  


def create_short_link(custom_id=None):
    main_url = 'http://127.0.0.1:5000/'
    if custom_id is None:
        custom_id = generate_custom_id()
    short_url = main_url + custom_id
    return short_url
    


@app.route('/')
def index_view():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_url_view():
    form = UrlForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        short = create_short_link(custom_id)
        short_url = URLMap(
            original=form.original.data,
            short=short
        )
        db.session.add(short_url)
        db.session.commit()
        return redirect(url_for('index_view', short_url=short))
    return render_template('index.html', form=form)