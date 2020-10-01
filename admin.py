#! /opt/venv/admin/bin/python

from config_flask import config, config_app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

app = config_app()


@app.errorhandler(404)
def page_not_found(error):
    return 'No se puede encontrar'


@app.route('/')
@app.route('/hello')
@login_required
def hello():
    name = current_user.id.capitalize()
    flash(f'Bienvenido {name}')
    return render_template('index.html')


if __name__ == "__main__":
    config()
    app.run(debug=True)
