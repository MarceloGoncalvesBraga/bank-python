
class Cliente:
    def __init__(self, nome,):
        self.nome = nome

    def getNome(self):
        return self.nome

    #def setNome(self, nome):
    #   self.nome = nome
        
    def toString(self):
        return f'Nome do Cliente :',self.getNome()