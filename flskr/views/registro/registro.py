from flask import Blueprint, render_template

registro_bp = Blueprint('registro', __name__, url_prefix = '/registro', template_folder='templates')

@registro_bp.route("/")
def registro_root():
    return render_template('registro.html')