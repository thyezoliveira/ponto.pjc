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
        
    def obter_lista_de_dias(self):
      dias = []
      for i in range(1, 31):
        dias.append(i)
      return dias
      
    def formatar_horario(self, reg:dict, current_reg_entrada:str):
      reg['reg_entrada'] = str(current_reg_entrada).zfill(4)[:2]+":"+str(current_reg_entrada).zfill(4)[2:]