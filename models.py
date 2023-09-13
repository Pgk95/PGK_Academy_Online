from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Define columuns for the User table
    username = db.Column(db.String(20), unique=True, nullable=False) # Username column
    email = db.Column(db.String(120), unique=True, nullable=False) # Email column
    password_hash = db.Column(db.String(60), nullable=False) # Password hash column
    fullname = db.Column(db.String(100), nullable=False) # Full name column

    # Set the table name to 'users'
    __tablename__ = 'users'