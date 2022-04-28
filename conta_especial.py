from conta_corrente import ContaCorrente

class ContaEspecial(ContaCorrente):
    
    def __init__(self, id, nome, saldo, limite):
        super().__init__(id, nome, saldo)
        self._limite = limite

    #def setLimite(self, limite):
    #    self._limite = limite
    def Depositar(self, valor):
        super().Depositar(valor)
        return True
    
    def getLImite(self):
        return self._limite
    
    def Sacar(self,valor):
        print(super().getSaldo())
        print(self._limite)
        #print(super())
        if (valor <= super().getSaldo()):
             #saldo = super().getSaldo() - valor
             #super().getSaldo(saldo)
             return True
        elif (valor <= int(super().getSaldo()) + int(self._limite)):
            limite = self._limite 
            #pega o total de saldo e desconta o emprestimo dentro do limite
            total_saldo =  super().getSaldo() - valor
            # subtrai o valor no limite 
            self._limite = self._limite + total_saldo
            
            super().setSaldo(total_saldo)

            return True
        elif (valor <= int(self._limite)):
            limite = self._limite 
            #pega o total de saldo e desconta o emprestimo dentro do limite
            total_saldo =  super().getSaldo() - valor
            # subtrai o valor no limite 
            self._limite = self._limite - valor
            
            super().setSaldo(total_saldo)

            return True
        else:
            print(" Saldo Insuficiente")
            return False
       
    def ToString(self):
         return f'Nome do Cliente :',super().getNome()
