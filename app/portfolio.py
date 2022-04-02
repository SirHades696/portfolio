# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    current_app,
    url_for
)
from .projects import projects
import sendgrid
from sendgrid.helpers.mail import *

bp = Blueprint('portfolio', __name__, url_prefix='/')
@bp.route('/', methods=['GET'])
def index():
    return render_template(
                            'portfolio/index.html', 
                            projects = projects)

@bp.route('/mail', methods = ['POST', 'GET'])
def send_mail():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if request.method == 'POST':
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')
    
    return redirect(url_for('portfolio.index'))

def send_email(name, email, message):
    mi_email =  'djnonasrm@gmail.com'
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(mi_email)
    to_email  = To(mi_email, substitutions= {
        "-name-": name,
        "-email-": email,
        "-message-": message,
    })
    
    content = Content(mime_type="text/html", content="""
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <title></title>
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
  <style>
    .cuerpo {
        font-family: sans-serif;
        background-color: #0d1117;
        width:100%;
    }
    
    .header {
        color: #0086cc;
        font-size:2rem;
        text-align: center;
    }
    
    p {
    	padding: 1rem 1rem 1rem 1rem;
      margin:1rem;
      margin-right:3rem;
      text-align: justify;
		  color: #efefef;
      font-size: 1.2rem;
      text-decoration:none;
    }
    
    .content {
        border: none;
        background-color: #2a3442;
        border-radius: 8px;
        box-shadow: 0 0 3px 3px rgba(239,239,239,0.3);
    }
  </style>
</head>
<body class="cuerpo">
<div align="center">
        <p></p>
        <p class="header">👽<b>SirHades696, tienes un nuevo contacto:</b></p>
        <p class="content"><b>Nombre:</b> -name-</p>
        <p class="content"><b>Correo:</b> -email-</p>
        <p class="content"><b>Mensaje:</b> -message-</p>
        <p></p>
</div>
</body>
</html>
    """)
    
    mail = Mail(mi_email, to_email, '👾Nuevo contacto desde la página web👾',html_content=content)
    response = sg.client.mail.send.post(request_body=mail.get())
    