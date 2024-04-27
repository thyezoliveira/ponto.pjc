from datetime import datetime
class Utils:
    def __init__(self):
        self.name = "Utilitários"
        self.version = 1.0
        self.info = self.criar_pacote()
    
    def criar_pacote(self):
        pacote = {
            "module_name":self.name,
            "module_version":self.version
        }
        return pacote
    
    def obter_ano_atual(self):
        agora = datetime.now()
        ano = agora.year
        return ano
    
    def obter_dia_atual(self):
        agora = datetime.now()
        dia = agora.day
        return dia
        
    def obter_mes_atual(self):
        agora = datetime.now()
        mes = agora.month
        return mes