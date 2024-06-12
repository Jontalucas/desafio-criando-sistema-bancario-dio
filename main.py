class Conta:
    def __init__(self, saldo):
        self.saldo = float(saldo)
        self.limiteSaque = 3
        self.historico = []
    def saque (self, valor):
        if self.saldo >= valor and self.limiteSaque > 0 and valor <= 500:
            self.saldo -= valor
            self.limiteSaque -= 1
            self.historico.append(-valor)
        elif valor > 500:
            print ("Valor excedeu o limite de saque!")
        elif self.limiteSaque == 0:
            print ("Limite de saques diário excedidos")
        else:
            print ("Saldo insuficiente")
            
    def deposito (self, valor):
        self.saldo += valor 
        self.historico.append(valor)
    def extrato (self):
        for valor in self.historico:
            if valor > 0:
                print(f'Depósito: R$ {float(valor):.2f}')
            else: 
                print(f'Saque: R$ {float(valor):.2f}')
        print(f'Saldo: R$ {float(self.saldo):.2f}' )
                
conta = Conta(1000)
opcoes = """
    1 - Ver Extrato
    2 - Saque
    3 - Depósito
    4 - Sair
"""
aux = True
while(aux == True):
    escolha = input(opcoes)
    if escolha == '1':
        conta.extrato()
    elif escolha == '2':
        valor = float(input("Digite o valor do saque: "))
        conta.saque(valor)
    elif escolha == '3':
        valor = float(input("Digite o valor do depósito: "))
        conta.deposito(valor)
    elif escolha == '4':
        aux = False
    else:
        print("Opção inválida")

