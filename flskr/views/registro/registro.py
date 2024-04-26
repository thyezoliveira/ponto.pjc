from flask import Blueprint

registro_bp = Blueprint('registro', __name__, url_prefix = '/registro')

@registro_bp.route("/")
def registro_root():
    return "Registro"