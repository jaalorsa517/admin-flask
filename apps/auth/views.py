from . import auth
from flask import request, redirect, render_template

@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('auth/login.html')


@auth.route('/singup', methods=['GET','POST'])
def singup():
    return 'singup'