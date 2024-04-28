from flask import Blueprint, render_template, request, redirect, url_for
from ...modules.database import Database
from ...modules.utils import Utils
from datetime import datetime, timedelta

registro_bp = Blueprint('registro', __name__, url_prefix = '/registro', template_folder='templates')
db = Database()

@registro_bp.route("/")
def registro_root():
  utils = Utils()
  dias_do_mes = utils.obter_lista_de_dias()
  res = db.obter_configuracoes()
  registros = db.obter_todos_os_registros()
  for reg in registros['list']:
    utils.formatar_horario(reg, reg['reg_entrada'])
  return render_template('registro.html', configs=res, registros=registros, dias_do_mes=dias_do_mes)

@registro_bp.post("/salvar")
def salvar_registro():
  data = {
    "reg_data":request.form['reg_data'],
    "reg_entrada":int(request.form['reg_entrada']),
    "reg_intervalo":int(100),
    "reg_saida":int(request.form['reg_saida']),
    "reg_carga_cumprida":- (int(request.form['reg_entrada'])+int(100)-int(request.form['reg_saida'])),
    "reg_atividade":request.form['reg_atividade']
  }
  res = db.inserir_um_novo_registro(**data)
  return redirect(url_for('app.registro.registro_root'))