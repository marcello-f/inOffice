from . import scheduler, db
from .models import User, Tracker

@scheduler.task('cron', id='do_reset', week="*", day_of_week="mon", hour=00, minute=00)
def scheduled_function():
    with scheduler.app.app_context():
        ids = [user.id for user in User.query.all()]
        for id in ids:
            data = Tracker.query.filter_by(user_id=id).first()
            new_mon = data.monday2
            new_tue = data.tuesday2
            new_wen = data.wednesday2
            new_thur = data.thursday2
            new_fri = data.friday2
            Tracker.query.filter_by(user_id=id).delete()
            new_data=Tracker(monday1=new_mon,tuesday1=new_tue,wednesday1=new_wen,thursday1=new_thur,friday1=new_fri,
            monday2=None,tuesday2=None,wednesday2=None,thursday2=None,friday2=None,user_id=id)
            db.session.add(new_data)
            db.session.commit()
            print("user data reset")