from flask import render_template, request, redirect, url_for, flash, session, Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .contact import send_email
from .models import User, db
import os
import smtplib


load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kalu:084612@localhost/pgkacademydb'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)


bcrypt = Bcrypt()

@app.route('/', strict_slashes=False)
def index():
    username = session.get('username')
    return render_template("index.html", username=username)


@app.route('/course', strict_slashes=False)
def course():
    return render_template('courses.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')



@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password_input')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, email=email, fullname=fullname, password_hash=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('index'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'],)
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            session['username'] = username
            flash(f'Welcome, {username}!', 'success')
            return redirect(url_for('index'))
        else:
            print('Login failed. Please check your credentials.', 'error')
    return render_template('login.html') 


@app.route('/logout')
def logout():
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



if __name__ == '__main__':
    app.run(debug=True)