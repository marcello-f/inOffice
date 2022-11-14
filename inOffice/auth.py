from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        surname = request.form.get('surname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if len(password1) < 4 or len(password2) < 4:  # type: ignore
            flash('Passwords must be at least 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(firstname) < 1 or len(surname) < 1:  # type: ignore
            flash('Firstname and surname must be at least 1 character.', category='error')
        else:
            if user:
                flash('An account associated with this email address already exists.', category='error')
                return redirect(url_for('auth.signup'))
            else:
                new_user = User(email=email, firstname=firstname, surname=surname, password=generate_password_hash(password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember='True')
                flash('Account has been successfully created!', category='success')
                return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember='True')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Please try again.', category="error") 
        else:
            flash('This email address is not associated with an account.', category="error") 
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))