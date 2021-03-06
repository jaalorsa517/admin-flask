from . import auth
from flask import request, redirect, render_template, url_for, flash
from forms import UserForm
from models.users import User
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    login_form = UserForm()
    context = dict(login_form=login_form)
    flash('Ingrese')
    return render_template('auth/login.html', **context)


@auth.route('/login', methods=['POST'])
def loginPost():
    login_form = UserForm()
    if login_form.validate_on_submit():
        nickname = login_form.nickname.data
        password = login_form.password.data
        user = User.getUser(nickname)
        if user is not None and check_password_hash(user.password, password):
            login_user(user)
            flash('Ingreso correcto')
            if bool(int(user.role)):
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('hello'))
        flash('Usuario o contraseña inválida')
    return redirect(url_for('auth.login'))


@auth.route('/singup')
def singup():
    context = dict(singup_form=UserForm())
    flash('Regístrese')
    return render_template('auth/singup.html', **context)


@auth.route('/singup', methods=['POST'])
def singupPost():
    singup_form = UserForm()
    if singup_form.validate_on_submit():
        nickname = singup_form.nickname.data
        if User.getUser(nickname) is None:
            password = generate_password_hash(singup_form.password.data)
            User.setUser(nickname, password)
            flash('Usuario creado')
            return redirect(url_for('auth.login'))
        else:
            flash('Usario ya existe')
    return redirect(url_for('auth.singup'))
