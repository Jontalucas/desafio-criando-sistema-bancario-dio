class Cliente:
    def __init__(self, nome, cpf, dataNascimento, logradouro, numero, bairo, cidade, uf):
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.endereco = logradouro + ' - ' + numero + ' - ' + bairo + ' - ' + cidade + '/' + uf
    def mostrarCliente(self):
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Data de Nascimento: {self.dataNascimento}')
        print(f'Endereço: {self.endereco}')
class Conta:
    def __init__(self, numero, cliente = Cliente):
        self.numero = numero
        self.saldo = float(0)
        self.limiteSaque = 3
        self.historico = []
        self.cliente = cliente
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
    def mostrarConta(self):
        print("Numero: " + str(self.numero))
        print(f"Saldo: R$ {float(self.saldo):.2f}")
        print("Cliente: " + self.cliente.nome)

def cadastrarCliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("CPF já cadastrado")
            return
    dataNascimento = input("Digite a data de nascimento do cliente: ")
    logradouro = input("Digite o logradouro do cliente: ")
    numero = input("Digite o número do cliente: ")
    bairo = input("Digite o bairro do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    uf = input("Digite a UF do cliente: ")
    cliente = Cliente(nome, cpf, dataNascimento, logradouro, numero, bairo, cidade, uf)
    clientes.append(cliente)
def criarConta():
    aux = False
    numero = input("Numero da Conta: ")
    for conta in contas:
        if conta.numero == numero:
            print("Numero de conta já existe")
            return
    nome = input("Dono da Conta: ")
    for cliente in clientes:
        if cliente.nome == nome:
            conta = Conta(numero, cliente)
            contas.append(conta)
            print("Conta criada com sucesso")
            aux = True
            return
    if aux == False:
        print("Cliente não encontrado")
        return
    
operacoes = """
    1 - Ver Extrato
    2 - Saque
    3 - Depósito
    4 - Voltar
"""
opcoes = """
    1 - Cadastrar Cliente
    2 - Criar Conta
    3 - Listar clientes
    4 - Listar contas
    5 - Fazer operacoes em uma conta
    6 - Sair
"""
contas = []
clientes = []
print ("Cadastre um cliente")
cadastrarCliente()
print ("Crie uma conta")
criarConta()
while True:
    escolhaOpcoes = input(opcoes)
    if escolhaOpcoes == "1":
        cadastrarCliente()
    elif escolhaOpcoes == "2":
        criarConta()
    elif escolhaOpcoes == "3":
        for cliente in clientes:
            cliente.mostrarCliente()
    elif escolhaOpcoes == "4":
        for conta in contas:
            conta.mostrarConta()
    elif escolhaOpcoes == "5":
        conta = None
        num = input("Digite o numero da conta")
        for c in contas:
            if c.numero == num:
                conta = c
        if conta == None:
            print("Conta não encontrada")
        else:
            while True:    
                escolhaOperacoes = input(operacoes)
                if escolhaOperacoes == '1':
                    conta.extrato()
                elif escolhaOperacoes == '2':
                    valor = float(input("Digite o valor do saque: "))
                    conta.saque(valor)
                elif escolhaOperacoes == '3':
                    valor = float(input("Digite o valor do depósito: "))
                    conta.deposito(valor)
                elif escolhaOperacoes == '4':
                    break
                else:
                    print("Opção inválida")
    elif escolhaOpcoes == "6":
        break
    else:
        print("Opção inválida")

