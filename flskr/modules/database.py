from ..models import Cabecalho_configs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        self._DATABASE_URI = 'sqlite:///ponto_pjc.db'
        self.engine = create_engine(self._DATABASE_URI)
        self.criar_configuracao_padrao()
        
    def criar_configuracao_padrao(self) -> None:
        session = sessionmaker(bind=self.engine)()
        conf_padrao = session.query(Cabecalho_configs).first()
        if not conf_padrao:
            conf_padrao = Cabecalho_configs(
                cbc_estudante = "Thyez de Oliveira",
                cbc_matricula = 0,
                cbc_curso = "Eng Soft",
                cbc_periodo = 6,
                cbc_ies = "UNICSUL - Universidade Cruzeiro do Sul",
                cbc_modalidade = "EAD",
                cbc_local_estagio = "Smecict - sala 15/B",
                cbc_supervisor = "Rosana Gildo",
                cbc_mes = 4,
                cbc_ano = 2024,
                )
            session.add(conf_padrao)
            session.commit()
            print("Configuracoes padroes definidas e registradas.")
    
    def obter_configuracoes(self) -> dict:
        session = sessionmaker(bind=self.engine)()
        db_configs = session.query(Cabecalho_configs).first()
        configuracao = {
            "cbc_estudante":db_configs.cbc_estudante,
            "cbc_matricula": db_configs.cbc_matricula,
            "cbc_curso":db_configs.cbc_curso,
            "cbc_periodo":db_configs.cbc_periodo,
            "cbc_ies":db_configs.cbc_ies,
            "cbc_modalidade":db_configs.cbc_modalidade,
            "cbc_local_estagio":db_configs.cbc_local_estagio,
            "cbc_supervisor"db_configs.cbc_supervisor,
            "cbc_ano":db_configs.cbc_ano
        }
        return configuracao
    
    def definir_configuracoes(self, **kwargs) -> None:
        nome = kwargs['nome']
        
        return {"msg":"As novas configuracoes foram registradas."}
    
    def resetar_configuracoes(self) -> None:
        pass