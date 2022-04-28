from cliente import Cliente

class ContaCorrente(Cliente):
    
    def __init__(self, id, nome, saldo):
        super().__init__(nome)
        self.id = id
        self._saldo = saldo
        
    def getId(self):
        return self.id

    def Depositar(self, valor):
        self._saldo += valor
        return True
    
    def getSaldo(self):
        return self._saldo

    def setSaldo(self,valor):
      self._saldo = valor

    def Sacar(self,valor):
        if (valor > self.getSaldo()):
            print("Saldo Insuficiente")
        else:
            self._saldo += valor
            return True
        
    def Transferir(self ,id ,valor):
      
        ContaCorrente[id].Depositar(valor)
        return True


    def ToString(self):
         return f'Nome do Cliente :',super().getNome()
