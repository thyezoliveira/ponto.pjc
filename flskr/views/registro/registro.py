from flask import Blueprint, render_template
from ...modules.database import Database

registro_bp = Blueprint('registro', __name__, url_prefix = '/registro', template_folder='templates')
db = Database()

@registro_bp.route("/")
def registro_root():
    res = db.obter_configuracoes()
    return render_template('registro.html', configs=res)