from flask import Blueprint, render_template, request

cabecalho_bp = Blueprint('cabecalho', __name__, url_prefix = '/cabecalho', template_folder='templates')

@cabecalho_bp.route("/")
def cabecalho_root():
    return render_template('cabecalho.html')
    
@cabecalho_bp.route('/salvar')
def salvar_cabecalho():
    test = request.args.get('test')
    return f"salvo -> {test}"