from flask import Flask


app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app) # Compliant

from application import routes


