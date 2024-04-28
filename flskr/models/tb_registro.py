from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DATABASE_URI = 'sqlite:///ponto_pjc.db'
Base = declarative_base()

class Registros(Base):
    __tablename__ = 'tb_registros'

    reg_id = Column(Integer, primary_key=True, autoincrement=True)
    reg_timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    reg_data = Column(Integer)
    reg_entrada = Column(Integer)
    reg_intervalo = Column(Integer)
    reg_saida = Column(Integer)
    reg_carga_cumprida = Column(Integer)
    reg_atividade = Column(String(150))

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
print("Tabela 'tb_registros' criada com sucesso no banco de dados 'ponto_pjc.db'.")