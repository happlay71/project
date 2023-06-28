import os
from flask import Blueprint

main = Blueprint('main', __name__, static_folder=os.path.join(os.path.abspath(os.path.dirname(__file__))
                                                              , '..', 'static'))

from . import views, errors, forms

