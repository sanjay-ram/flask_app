from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Data7Dollar$@localhost:3306/flask_software'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    profile = db.relationship('UserProfile', backref='user', uselist=False)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Adding a new user and profile
with app.app_context():
    try:
        new_user = User(name='John Doe', email='john@example.com')
        db.session.add(new_user)

        user_profile = UserProfile(bio='Hello, I am John!', profile_picture='path/to/picture.jpg', user=new_user)
        db.session.add(user_profile)

        db.session.commit()
        print("Data inserted successfully.")
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred: {e}")

# Querying users
with app.app_context():
    users = User.query.all()
    for user in users:
        print(f'User: {user.name}, Email: {user.email}, Bio: {user.profile.bio if user.profile else "No profile"}')