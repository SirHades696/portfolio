# -*- coding: utf-8 -*-
__author__ = "SirHades696"
__email__ = "djnonasrm@gmail.com"

from flask import Blueprint, render_template, request, redirect, current_app, url_for
from .projects import projects
from .linux_projects import linux_projects
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .html_template import *

bp = Blueprint("portfolio", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def index():
    return render_template(
        "portfolio/index.html", projects=projects, linux_projects=linux_projects
    )


@bp.route("/mail", methods=["POST", "GET"])
def send_mail():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    data_message = {"name":name, "email":email, "message":message}
    if request.method == "POST":
        send_email(data_message)

def send_email(data_message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = current_app.config["EMAIL_DEST"]
    password = current_app.config["PSWD"]
    receiver_email = current_app.config["EMAIL_DEST"]
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = '👾Nuevo contacto desde la página web👾'
    body = template.format(name=data_message["name"], 
                            email=data_message["email"], 
                            message=data_message["message"])
    message.attach(MIMEText(body, 'html'))
    try:
      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(sender_email, password)
      text = message.as_string()
      server.sendmail(sender_email, receiver_email, text)
      return render_template("portfolio/sent_mail.html")
    except smtplib.SMTPException as e:
      return redirect(url_for("portfolio.index"))
    finally:
      server.quit()