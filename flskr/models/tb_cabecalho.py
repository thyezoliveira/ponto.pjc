from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///ponto_pjc.db'
Base = declarative_base()

class Cabecalho_configs(Base):
    __tablename__ = 'tb_cabecalho'

    cbc_id = Column(Integer, primary_key=True, autoincrement=True)
    cbc_estudante = Column(String(100))
    cbc_matricula = Column(Integer)
    cbc_curso = Column(String(100))
    cbc_periodo = Column(Integer)
    cbc_ies = Column(String(100))
    cbc_modalidade = Column(String(15))
    cbc_local_estagio = Column(String(150))
    cbc_supervisor = Column(String(100))
    cbc_mes = Column(Integer)
    cbc_ano = Column(Integer)

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
print("Tabela 'tb_cabecalho' criada com sucesso no banco de dados 'ponto_pjc.db'.")