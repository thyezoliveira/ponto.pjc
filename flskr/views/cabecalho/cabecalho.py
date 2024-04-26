from flask import Blueprint

cabecalho_bp = Blueprint('cabecalho', __name__, url_prefix = '/cabecalho')

@cabecalho_bp.route("/")
def cabecalho_root():
    return "Cabecalho"