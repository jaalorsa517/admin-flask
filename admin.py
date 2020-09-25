#! /opt/venv/admin/bin/python

from config_flask import config, config_app
from flask import render_template, request

app = config_app()

@app.route('/')
def root():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found():
    return 'No se puede encontrar'

if __name__ == "__main__":
    config()
    app.run()

