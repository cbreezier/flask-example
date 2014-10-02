from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import login_user, logout_user, current_user

from app import db
from app import login_manager
from app.myapp.models import User
from app.myapp.forms import LoginForm, RegisterForm

myapp = Blueprint('myapp', __name__)

@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(id=userid).first()

@myapp.route('/')
def show_users():
    users = User.query.all()
    logged_in = current_user

    return render_template('myapp/show_users.html', title='Users', users=users, logged_in=logged_in)

@myapp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user and user.check_password(request.form['password']):
                login_user(user)
                return redirect(url_for('myapp.show_users'))
            else:
                error = 'Incorrect username or password'
        else:
            error = 'Form validation error'

    return render_template('myapp/login.html', error=error, form=form)

@myapp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('myapp.show_users'))

@myapp.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login_user(user)
            return redirect(url_for('myapp.show_users'))
        else:
            error = 'Form validation error'

    return render_template('myapp/register.html', error=error, form=form)