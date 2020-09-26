#! /opt/venv/admin/bin/python

from config_flask import config, config_app
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

app = config_app()


@app.errorhandler(404)
def page_not_found(error):
    return 'No se puede encontrar'


@app.route('/')
def root():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    return render_template('index.html')


@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')


if __name__ == "__main__":
    config()
    app.run()
