from flask import Blueprint, render_template, request
from ...modules.database import Database

cabecalho_bp = Blueprint('cabecalho', __name__, url_prefix = '/cabecalho', template_folder='templates')
db = Database()

@cabecalho_bp.route("/")
def cabecalho_root():
    res = db.obter_configuracoes()
    return render_template('cabecalho.html', configs=res)
    
@cabecalho_bp.route('/salvar', methods=["POST"])
def salvar_cabecalho():
    nome = request.form.get('nome')
    res = db.definir_configuracoes(nome=nome)
    return f"resposta do servidor -> {res}"