from flask import Blueprint, render_template
from .registro import registro_bp
from .cabecalho import cabecalho_bp
from ..modules.database import Database

db = Database()
app_bp = Blueprint('app', __name__, url_prefix = '/app', template_folder="templates")

app_bp.register_blueprint(registro_bp)
app_bp.register_blueprint(cabecalho_bp)

@app_bp.route("/")
def ponto_app():
    res = db.obter_configuracoes()
    return render_template("index.html", configs=res)