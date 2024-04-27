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
            "cbc_id":db_configs.cbc_id,
            "cbc_estudante":db_configs.cbc_estudante,
            "cbc_matricula": db_configs.cbc_matricula,
            "cbc_curso":db_configs.cbc_curso,
            "cbc_periodo":db_configs.cbc_periodo,
            "cbc_ies":db_configs.cbc_ies,
            "cbc_modalidade":db_configs.cbc_modalidade,
            "cbc_local_estagio":db_configs.cbc_local_estagio,
            "cbc_supervisor":db_configs.cbc_supervisor,
            "cbc_mes":db_configs.cbc_mes,
            "cbc_ano":db_configs.cbc_ano
        }
        return configuracao
    
    def definir_configuracoes(self, cbc_id:int, **kwargs) -> None:
        session = sessionmaker(bind=self.engine)()
        configs = session.query(Cabecalho_configs).filter_by(cbc_id=cbc_id).first()
        configs.cbc_estudante = kwargs['cbc_estudante']
        configs.cbc_matricula = kwargs['cbc_matricula']
        configs.cbc_curso = kwargs['cbc_curso']
        configs.cbc_periodo = kwargs['cbc_periodo']
        configs.cbc_ies = kwargs['cbc_ies']
        configs.cbc_modalidade = kwargs['cbc_modalidade']
        configs.cbc_local_estagio = kwargs['cbc_local_estagio']
        configs.cbc_supervisor = kwargs['cbc_supervisor']
        configs.cbc_mes = kwargs['cbc_mes']
        configs.cbc_ano = kwargs['cbc_ano']
        session.commit()
        session.close()
        
        return {"msg":f"As novas configuracoes foram registradas. Para o id {cbc_id}"}
    
    def resetar_configuracoes(self) -> None:
        pass