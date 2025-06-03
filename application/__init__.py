from flask import Flask
from fastapi_csrf_protect import CsrfProtect


app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app) # Compliant

from application import routes


