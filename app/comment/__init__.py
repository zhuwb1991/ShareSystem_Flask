from flask import Blueprint

comment = Blueprint('comment', __name__, url_prefix='/add_comment/')

from . import views