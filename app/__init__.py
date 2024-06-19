# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        EMAIL_DEST=os.environ.get("EMAIL_DEST"),
        PSWD=os.environ.get("PSWD"),
    )
    
    from . import portfolio
    
    app.register_blueprint(portfolio.bp)
    
    return app