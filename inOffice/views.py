from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user
from sqlalchemy import update
from .models import User
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@views.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        surname = request.form.get('surname')

        email_check = User.query.filter_by(email=email).first()
        if email_check:
                flash('An account associated with this email address already exists.', category='error')
                return redirect(url_for('views.edit_profile'))
        elif len(firstname) < 1 or len(surname) < 1:  # type: ignore
            flash('Firstname and surname must be at least 1 character.', category='error')
        else:
            update_user = User.query.filter_by(id=current_user.id).first()
            update_user.email=email
            update_user.firstname=firstname
            update_user.surname=surname
            db.session.commit()
            flash('Account details have been successfully updated!', category='success')
            return redirect(url_for('views.profile'))
    return render_template('edit-profile.html', user=current_user)

@views.route('/deletion', methods=['GET', 'POST'])
@login_required
def deletion():
    if request.method == 'POST':
        ticked = request.form.get('delete')
        user_id = current_user.id
        if ticked:
            logout_user()
            User.query.filter_by(id=user_id).delete()
            db.session.commit()
            flash('Account has been successfully deleted.', category='success')
            return redirect(url_for('auth.login'))
        else:
            flash('To delete account please check the box.', category='error')
            return redirect(url_for('views.profile'))
    return render_template('deletion.html', user=current_user)