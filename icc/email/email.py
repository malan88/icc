"""Send an email system."""
from threading import Thread
from flask_mail import Message
from flask import render_template, current_app
from icc import mail


def send_async_email(app, msg):
    """Send an email in a new thread!"""
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    """Send an email."""
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app, msg)).start()


def send_password_reset_email(user):
    """Send a password reset email."""
    token = user.get_reset_password_token()
    send_email('anno.wiki - Reset Your Password',
               sender=current_app.config['ADMINS'][0], recipients=[user.email],
               text_body=render_template('email/reset_password.txt', user=user,
                                         token=token),
               html_body=render_template('email/reset_password.html', user=user,
                                         token=token)
               )
