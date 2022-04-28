class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    #def setNome(self, nome):
    #   self.nome = nome
        
    def toString(self):
        return f'Nome do Cliente :',self.getNome()
    
class ContaCorrente(Cliente):

    def __init__(self, id, nome, saldo):
        super().__init__(nome)
        self._saldo = saldo

    def Depositar(self, valor):
        self._saldo += valor

    def getSaldo(self):
        return self._saldo

    def ToString(self):
        return f'Nome do Cliente :',super().getNome()

class ContaEspecial(ContaCorrente):

    def __init__(self, id, nome, saldo, limite):
        super(self).__init__(self,id, nome, saldo)
        self._limite = limite

    #def setLimite(self, limite):
    #    self._limite = limite

    def getLImite(self):
        return self.limite
    
    def tipoEntrega(self):
        return super().tipoEntrega()
    
    def ToString(self):
        return f'Nome do Cliente :',super().getNome()

lista_clientes_nome = [
    Cliente("Julia"),
    Cliente("Ana"),
    Cliente("Paulo"),
    Cliente("Andre")
]

nome = ContaCorrente(1,lista_clientes_nome[0].getNome(),0)
   
print(nome.getNome())

#funcionario = ContaEspecial("Josue", "99881122", "josue@gmail.com", "123456", 1000)

#print(f"Nome do Funcionário = {funcionario.getNome()}")
