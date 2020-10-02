#! /opt/venv/admin/bin/python

from config_flask import config, config_app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.users import User
from forms import TableForm, RowForm

app = config_app()


@app.errorhandler(404)
def page_not_found(error):
    return 'No se puede encontrar'


@app.route('/admin')
@login_required
def admin():
    users= User.getUsers()
    form_users = TableForm()
    for row in users:
        _row = RowForm()
        _row.nickname = row['name']
        _row.check = bool(int(row['role']))
        form_users.rows.append_entry(_row)
    context = dict(users = users, form_user = form_users)
    return render_template('admin.html',**context)

@app.route('/admin', methods =['POST'])
def adminPost():
    table_form = TableForm()
    # import pdb; pdb.set_trace()
    if table_form.validate_on_submit():
        print(table_form.rows.data)
    return redirect(url_for('admin'))

@app.route('/')
@login_required
def hello():
    name = current_user.id.capitalize()
    flash(f'Bienvenido {name}')
    return render_template('index.html')


if __name__ == "__main__":
    config()
    app.run(debug=True)
