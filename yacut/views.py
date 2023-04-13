from flask import abort, flash, redirect, render_template

from yacut.forms import UrlForm
from yacut.models import URLMap
from yacut.utils import check_custom_id_exists, create_short_link

from . import app, db

main_url = 'http://localhost/'

@app.route('/<path:custom_id>', methods=['GET'])
def redirect_view(custom_id):
    short_url = check_custom_id_exists(custom_id)
    if short_url is not None:
        original_url = short_url.original
        return redirect(original_url)
    abort(404)


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        # print('форма валидна')
        custom_id = form.custom_id.data
        if custom_id is None or len(custom_id) == 0:
            short_url, custom_id = create_short_link()
        else:
            if check_custom_id_exists(custom_id):
                flash(f'Имя {custom_id} уже занято!')
                return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        short_url = main_url + custom_id
        db.session.add(urlmap)
        db.session.commit()
        return render_template('index.html', short_url=short_url, form=form)
    return render_template('index.html', form=form)