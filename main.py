from asyncio.windows_events import NULL
from asyncore import ExitNow
from tracemalloc import stop
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_especial import ContaEspecial

lista_clientes_nome = [
    Cliente("Erika"),
    Cliente("Marcelo"),
    Cliente("Paulo"),
    Cliente("Andre")
]
lista_clientes_contas = [
    ContaCorrente(1,lista_clientes_nome[0].getNome(),0),
    ContaCorrente(2,lista_clientes_nome[1].getNome(),0),
    ContaCorrente(3,lista_clientes_nome[2].getNome(),0),
    ContaCorrente(4,lista_clientes_nome[3].getNome(),0),
]
lista_clientes_contas_especial = [
    ContaEspecial(1,lista_clientes_nome[0].getNome(),0,500),
    ContaEspecial(2,lista_clientes_nome[1].getNome(),0,1000),
    ContaEspecial(3,lista_clientes_nome[2].getNome(),0,700),
    ContaEspecial(4,lista_clientes_nome[3].getNome(),0,1500),
]
#def main():
def Logo():
    print("\n\t-------------------------------------")
    print("\t           BANCO PRINCIPAL            ")
    print("\t-------------------------------------")
    
def MenuAbrirConta():
    Logo()
    print("\t 1 - Conta Corrente ")
    print("\t 2 - Conta Especial ")   
    print("\t 6 - Sair ")
    print("\t-------------------------------------\n")
def MenuConta():
    Logo()
    print("\t 1 - Depositar ")
    print("\t 2 - Sacar ")
    print("\t 3 - Consultar Saldo")
    print("\t 4 - Tranferir ") 
    print("\t 6 - Sair ")
    print("\t-------------------------------------\n")

def MenuAcesso(contas):
    Logo()
    if contas == 0:
     print("\t CLIENTE SEM CONTA NO BANCO ")
     print("\t DESEJA ABRIR CONTA OPCAO 5 ")
    elif contas == 1 :
      print("\t 1 - Conta Corrente ")
    elif contas == 2:
      print("\t 2 - Conta Especial ")
    elif contas == 3:
      print("\t 1 - Conta Corrente ")
      print("\t 2 - Conta Especial ")
      
    print("\t 6 - Sair ")
    print("\t-------------------------------------\n")
def ContaOff():
      Logo()
      print("\t        CLIENTE-NÃO-ENCONTRADO     \n")
      print("\t   5  -  DESEJA ABRIR CONTA      \n")
      print("\t   6  -  SAIR           ")
def Sair():
      exit()
def ConsultaContas(nome):
    contas = 0;
    while True:
     for user in lista_clientes_contas:
      if (user.getNome() == nome):
        contas = contas + 1
     for user in lista_clientes_contas_especial:
        if (user.getNome() == nome):
            contas = contas + 2
     return MenuAcesso(contas)
     #break
def EntrouContaCorrente(nome):
       nome = nome
       while True:
            MenuConta();
            for user in lista_clientes_contas:
                if(user.getNome() == nome):
                  opcao = int(input("Digite a opção desejada: "))
                  if opcao == 1: 
                    valor = int(input("Digite o valor: "))
                    user.Depositar(valor)
                  elif opcao == 2:         
                    valor = int(input("Digite o valor: "))
                    user.Sacar(valor)
                  elif opcao == 3:
                    Logo();
                    saldo = user.getSaldo();
                    print("\t SALDO DE R$: ", saldo)
                  elif opcao == 4 :
                    valor = int(input("Digite o valor: "))
                    conta = int(input("Digite a Conta: "))
                    user.Transferir(valor,conta)
                  elif opcao == 6:
                   exit()
                  else:
                      print("Opcao Invalida")

def EntrouContaEspecial(nome):
       nome = nome
       while True:
            MenuConta();
            print("\t-----------------------CLIENTE-VIP---\n")
            for user in lista_clientes_contas_especial:
              if(user.getNome() == nome):
                  opcao = int(input("Digite a opção desejada: "))
                  if opcao == 1: 
                    valor = int(input("Digite o valor: "))
                    user.Depositar(valor)
                  elif opcao == 2:         
                    valor = int(input("Digite o valor: "))
                    user.Sacar(valor)
                  elif opcao == 3:
                    Logo();
                    saldo = user.getSaldo();
                    print("\t SALDO DE R$: ", saldo)
                    print(f"\tLIMITE-CHEQUE-ESPECIAL- R$: {user.getLimite()}")
                    print("\t-----------------------------------")
                  elif opcao == 4 :
                    valor = int(input("Digite o valor: "))
                    conta = int(input("Digite a Conta: "))
                    user.Transferir(valor,conta)
                  elif opcao == 6:
                   exit()
                  else:
                      print("Opcao Invalida")

def AbrirConta(nome_cliente):
    ContaCorrente(1,lista_clientes_nome[0].getNome(),0),       
def valide(nome):
    if nome == '':
      return False
    elif nome == 0:
      return False
    else:
      return True
def Conta():
  while True:
    cliente = NULL
    nome_cliente = input("Digite o Nome do Cliente: ")
    nome_cliente.split(' ')
    if valide(nome_cliente):
        try:  
          for user in lista_clientes_nome:  
           if(user.getNome() == nome_cliente):
            cliente = user.getNome()
          if(cliente == NULL):
            ContaOff()
            opcao = int(input("Digite a opção desejada: \n"))
            if opcao == 5: 
             AbrirConta(cliente)
            elif opcao ==6:
             Sair()
          print("\t Conta Encontrada: ",cliente," \t")
          ConsultaContas(cliente)
          opcao_conta = int(input("Digite a opção desejada: \n"))
          
          if opcao_conta == 1: 
                EntrouContaCorrente(user.getNome());
          elif opcao_conta ==2:
                EntrouContaEspecial(user.getNome());
          elif opcao_conta ==6:
            break
        except:
          Logo()
          
    else: 
      Logo()
      print("Dgite um nome Válido !")
      
Conta()

#print(lista_clientes_contas_especial[1].getLImite() )
