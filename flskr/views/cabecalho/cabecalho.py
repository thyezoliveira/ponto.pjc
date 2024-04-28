from flask import Blueprint, render_template, request, redirect, url_for
from ...modules.database import Database
from ...modules.utils import Utils

cabecalho_bp = Blueprint('cabecalho', __name__, url_prefix = '/cabecalho', template_folder='templates')
db = Database()

@cabecalho_bp.route("/")
def cabecalho_root():
    res = db.obter_configuracoes()
    registros = db.obter_todos_os_registros()
    utils = Utils()
    mes = utils.obter_mes_atual()
    ano = utils.obter_ano_atual()
    return render_template('cabecalho.html', configs=res, mes_atual=mes, ano_atual=ano, registros=registros)
    
@cabecalho_bp.route('/salvar', methods=["POST"])
def salvar_cabecalho():
    cbc_id = db.obter_configuracoes()["cbc_id"]
    save_configs = {
        "cbc_estudante":request.form.get('cbc_estudante'),
        "cbc_matricula":request.form.get('cbc_matricula'),
        "cbc_curso":request.form.get('cbc_curso'),
        "cbc_periodo":request.form.get('cbc_periodo'),
        "cbc_ies":request.form.get('cbc_ies'),
        "cbc_modalidade":request.form.get('cbc_modalidade'),
        "cbc_local_estagio":request.form.get('cbc_local_estagio'),
        "cbc_supervisor":request.form.get("cbc_supervisor"),
        "cbc_mes":request.form.get("cbc_mes"),
        "cbc_ano":request.form.get("cbc_ano")
    }
    res = db.definir_configuracoes(cbc_id, **save_configs)
    return redirect(url_for("app.cabecalho.cabecalho_root"))