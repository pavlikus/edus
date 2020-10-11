from django.core.mail import send_mail

from edus.celery import app


@app.task
def send_email(subject, message, from_email, recipients):
    send_mail(subject, message, from_email, recipients)
