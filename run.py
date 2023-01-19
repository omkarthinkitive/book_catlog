from app import create_app, db  # from the app package __init__
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        
        if not User.query.filter_by(user_name='sahil').first():
            User.create_user(user='sahil',
                             email='sahil@gmail.com',
                             password='root')
        
    flask_app.run()
