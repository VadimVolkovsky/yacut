from flask import abort, flash, redirect, render_template

from settings import INDEX_URL, MAIN_PAGE_TEMPLATE, MAIN_URL, REDIRECT_URL
from yacut.forms import UrlForm
from yacut.models import URLMap
from . import app, db


@app.route(REDIRECT_URL, methods=['GET'])
def redirect_view(custom_id):
    urlmap = URLMap.check_custom_id_exists(custom_id)
    if urlmap is not None:
        original_url = urlmap.original
        return redirect(original_url)
    abort(404)


@app.route(INDEX_URL, methods=['GET', 'POST'])
def index_view():
    form = UrlForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id is None or len(custom_id) == 0:
            custom_id = URLMap.generate_custom_id()
            short_url = URLMap.create_short_link(custom_id)
        else:
            if URLMap.check_custom_id_exists(custom_id):
                flash(f'Имя {custom_id} уже занято!')
                return render_template(MAIN_PAGE_TEMPLATE, form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id
        )
        short_url = MAIN_URL + custom_id
        db.session.add(urlmap)
        db.session.commit()
        return render_template(MAIN_PAGE_TEMPLATE, short_url=short_url, form=form)
    return render_template(MAIN_PAGE_TEMPLATE, form=form)