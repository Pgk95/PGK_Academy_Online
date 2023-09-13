# import neccessary modules
from flask import render_template, request, redirect, url_for, flash, session, Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .contact import send_email
from .models import User, db
import os
import smtplib

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure the Flask app with database URI and secret key from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CRIDENTIALS')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Intialize SQLAlchemy
db.init_app(app)

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt()

# Definethe route for the homepage 
@app.route('/', strict_slashes=False)
def index():
    username = session.get('username')
    return render_template("index.html", username=username)


# Define the route for the course page
@app.route('/course', strict_slashes=False)
def course():
    return render_template('courses.html')

# Define the route for the about page
@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


# Define the route for user registration (signup)
@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password_input')

        # Hash the user's password before storing it
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new User object and add it to the database
        new_user = User(username=username, email=email, fullname=fullname, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html')


# Define the route for user login
@app.route('/login', methods=['GET', 'POST'],)
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database to check if the user exists and the password is correct
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            # Set a session variable to track the user's login status
            session['username'] = username
            flash(f'Welcome, {username}!', 'success')
            return redirect(url_for('index'))
        else:
            print('Login failed. Please check your credentials.', 'error')
    return render_template('login.html') 


# Define the route for logout
@app.route('/logout')
def logout():
    # Clear the user's session data to log them out
    session.clear()
    flash('you have been logged out','success')
    return redirect(url_for('index'))


@app.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        send_email(name, email, message)

        return render_template('thank_you.html')
    else:
        return render_template('contact.html')


# Run the flask application ifthis script is executed directly
if __name__ == '__main__':
    app.run(debug=True)