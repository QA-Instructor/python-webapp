from flask import Flask
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app) # Compliant

from application import routes


