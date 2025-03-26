from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    joined_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

# ✅ Run inside the application context
with app.app_context():
    db.create_all()

    # Create a new user
    if not User.query.filter_by(username='aj14jain').first():
        admin = User(username='aj14jain', email='aj14jain@ex.com')
        db.session.add(admin)
        db.session.commit()

    # Retrieve all users
    users = User.query.all()
    results = [{"username": user.username, "email": user.email} for user in users]
    print("Users:", results)

    # Query by username
    users = User.query.filter_by(username='aj14jain').all()

    # ✅ Use `db.session.get()` instead of `Query.get()`
    user = db.session.get(User, 1)
    if user:
        result = {"username": user.username, "email": user.email}
        print("Queried User:", result)

    # Query Books (if any exist)
    fields = ["id", "name", "author"]
    field_objects = [getattr(Book, field) for field in fields]
    books = Book.query.with_entities(*field_objects).all()
    print("Books:", books)

    # Update a user
    User.query.filter_by(id=1).update({"username": "aj14jain"})
    db.session.commit()

    # ✅ Use `db.session.get()` for deletion
    user = db.session.get(User, 1)
    if user:
        db.session.delete(user)
        db.session.commit()
        print("User deleted.")