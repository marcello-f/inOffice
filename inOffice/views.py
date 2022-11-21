from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user
from sqlalchemy import update
from .models import User, Tracker
import datetime
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        monday1 = request.form.get('monday1')
        tuesday1 = request.form.get('tuesday1')
        wednesday1 = request.form.get('wednesday1')
        thursday1 = request.form.get('thursday1')
        friday1 = request.form.get('friday1')
        monday2 = request.form.get('monday2')
        tuesday2 = request.form.get('tuesday2')
        wednesday2 = request.form.get('wednesday2')
        thursday2 = request.form.get('thursday2')
        friday2 = request.form.get('friday2')

        check = Tracker.query.filter_by(user_id=current_user.id).count()
        print(check)
        if check == 1:
            Tracker.query.filter_by(user_id=current_user.id).delete()
            new_data=Tracker(monday1=monday1,tuesday1=tuesday1,wednesday1=wednesday1,thursday1=thursday1,friday1=friday1,
            monday2=monday2,tuesday2=tuesday2,wednesday2=wednesday2,thursday2=thursday2,friday2=friday2,user_id=current_user.id)
            db.session.add(new_data)
            db.session.commit()
            flash('Your office days have been updated!', category='success')
            return redirect(url_for('views.home'))
        else:
            new_data=Tracker(monday1=monday1,tuesday1=tuesday1,wednesday1=wednesday1,thursday1=thursday1,friday1=friday1,
            monday2=monday2,tuesday2=tuesday2,wednesday2=wednesday2,thursday2=thursday2,friday2=friday2,user_id=current_user.id)
            db.session.add(new_data)
            db.session.commit()
            flash('Your office days have been updated!', category='success')
            return redirect(url_for('views.home'))

    day = datetime.date.today()
    month = datetime.date.today().strftime("%B")
    weekday = datetime.date.today().strftime('%A')
    data = User.query.all()

    def weeks():
        dates = []
        
        if weekday == 'Monday':
            dates = [day + datetime.timedelta(days=i) for i in range(14)]
        elif weekday == 'Tuesday':
            dates = [day + datetime.timedelta(days=i-1)for i in range(14)]
        elif weekday == 'Wednesday':
            dates = [day + datetime.timedelta(days=i-2) for i in range(14)]
        elif weekday == 'Thursday':
            dates = [day + datetime.timedelta(days=i-3) for i in range(14)]
        elif weekday == 'Friday':
            dates = [day + datetime.timedelta(days=i-4) for i in range(14)]
        elif weekday == 'Saturday':
            dates = [day + datetime.timedelta(days=i-5) for i in range(14)]
        elif weekday == 'Sunday':
            dates = [day + datetime.timedelta(days=i-6) for i in range(14)]

        for i in range(len(dates)):
                if dates[i].day == 1 or dates[i].day == 21 or dates[i].day == 31:
                    dates[i] = str(dates[i]) + 'st'
                elif dates[i].day == 2 or dates[i].day == 22:
                    dates[i] = str(dates[i]) + 'nd'
                elif dates[i].day == 3 or dates[i].day == 23:
                    dates[i] = str(dates[i]) + 'rd'
                else:
                    dates[i] = str(dates[i]) + 'th'
        return dates

    return render_template('home.html', user=current_user, data=data, day=day, month=month, weekday=weekday, weeks=weeks())

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
            Tracker.query.filter_by(user_id=user_id).delete()
            db.session.commit()
            flash('Account has been successfully deleted.', category='success')
            return redirect(url_for('auth.login'))
        else:
            flash('To delete account please check the box.', category='error')
            return redirect(url_for('views.profile'))
    return render_template('deletion.html', user=current_user)