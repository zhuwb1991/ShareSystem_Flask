from flask import Blueprint

auto_test = Blueprint('auto_test', __name__, url_prefix='/auto_test/')

from . import views
