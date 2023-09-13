from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'pgkacademyonline@gmail.com'
app.config['MAIL_PASSWORD'] = 'buwjbqyguczhbtsn'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

def send_email(name, email, message):
    recipients = ['pgkacademyonline@gmail.com']
    msg = Message('New Contact Form Submission', sender='pgkacademyonline@gmail.com', recipients=recipients)
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(str(e))
        return False