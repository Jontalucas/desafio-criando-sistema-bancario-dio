from abc import ABC, abstractmethod

class Transacao(ABC):
    @property 
    @abstractmethod
    def valor(self):
        pass
    @abstractmethod
    def registrar(conta):
        pass

class Cliente:
    def __init__(self, logradouro, numero, bairo, cidade, uf):
        self._endereco = logradouro +' - '+ numero +' - '+ bairo +' - '+ cidade +'/'+ uf
        self._contas = []
    @property
    def nome(self):
        return self._nome
    @property
    def contas(self):
        return self._contas
    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionarConta(self, conta):
        self._contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, dataNascimento, logradouro, numero, bairo, cidade, uf):
        super().__init__(logradouro, numero, bairo, cidade, uf)
        self._nome = nome
        self._cpf = cpf
        self._dataNascimento = dataNascimento      
    def __str__(self):
        return f"Nome: {self._nome}\nCPF: {self._cpf}\nData de Nascimento: {self._dataNascimento}\nEndereço: {self._endereco}"

class Historico:
    def __init__(self):
        self._transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    def adicionarTransacao(self, transacao: Transacao):
        registro = f"{str(transacao.__class__.__name__)}: R$  {transacao.valor:.2f}"
        self.transacoes.append(registro)
        
class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._agencia = "001"
        self._saldo = 0
        self._historico = Historico()
        self._cliente = cliente
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def saldo(self):
        return self._saldo
    @property
    def historico(self):
        return self._historico
    @property
    def cliente(self):
        return self._cliente    
    @classmethod
    def novaConta(cls, num, cliente):
        return cls(num, cliente)
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        else:
            return False
    def depositar(self, valor):
        self._saldo += valor
        return True
    def verExtrato(self):
        for transacao in self.historico.transacoes:
            print(transacao)
        print(f"Saldo: R$ {float(self.saldo):.2f}")
    def __str__(self):
        return f"Numero: {self.numero}\nSaldo: R$ {float(self.saldo):.2f}\nAgencia: {self.agencia}\nCliente: {self.cliente.nome}"
class ContaCorrente(Conta):
    def __init__(self, numero, cliente,  limite=500, limiteSaques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limiteSaques = limiteSaques
    def sacar(self, valor):
        if self.saldo >= valor and self._limiteSaques > 0 and valor <= self._limite:
            self._saldo -= valor
            self._limiteSaques -= 1
            return True
        elif valor > self._limite:
            print ("Valor excedeu o limite de saque!")
        elif self._limiteSaques == 0:
            print ("Limite de saques diário excedidos")
        else:
            print ("Saldo insuficiente")
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return float(self._valor)
    def registrar(self, conta: Conta):
        transacaoSucedida = conta.depositar(self.valor)
        if transacaoSucedida:
            conta.historico.adicionarTransacao(self)
            
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    @property
    def valor(self):
        return float(self._valor)
    def registrar(self, conta: Conta):
        transacaoSucedida = conta.sacar(self.valor)
        if transacaoSucedida:
            conta.historico.adicionarTransacao(self)

clientes = []

opcoes = """
    1 - Cadastrar Cliente
    2 - Listar clientes
    3 - Fazer operacoes como cliente
    4 - Sair
"""
operacoesCliente = """
    1 - Criar conta
    2 - Listar Contas
    3 - Fazer operacoes em uma conta
    4 - Voltar
"""
operacoesConta = """
    1 - Ver Extrato
    2 - Saque
    3 - Depósito
    4 - Voltar
"""

while True:
    escolhaOpcoes = input(opcoes)
    if escolhaOpcoes == "1":
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        dataNascimento = input("Digite a data de nascimento: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o numero: ")
        bairo = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        uf = input("Digite a uf: ")
        cliente = PessoaFisica(nome, cpf, dataNascimento, logradouro, numero, bairo, cidade, uf)
        clientes.append(cliente)
    elif escolhaOpcoes == "2":
        for cliente in clientes:
            print (cliente)
    elif escolhaOpcoes == "3":
        while True:
            cliente = None
            escolhaCliente = input("Digite S para voltar\nDigite o nome do cliente: ")
            if escolhaCliente.lower() == 's':
                break
            else: 
                for c in clientes:
                    if c.nome == escolhaCliente:
                        cliente = c
                if cliente == None:
                    print("Cliente não existe")
                else:
                    while True:
                        escolhaOperacoesCliente = input(operacoesCliente)
                        if escolhaOperacoesCliente == "1":
                            jaExiste = False
                            numero = input("Numero da Conta: ")
                            for c in clientes:
                                for conta in c.contas:
                                    if conta.numero == numero:
                                        jaExiste = True
                            if jaExiste == False:
                                cliente.adicionarConta(ContaCorrente.novaConta(numero, cliente))
                            else:
                                print("Conta já existe")
                        elif escolhaOperacoesCliente == "2":
                            for conta in cliente.contas:
                                print(conta)
                        elif escolhaOperacoesCliente == "3":
                            while True:
                                conta = None
                                escolhaConta = input("Digite S para voltar\nDigite o numero da conta: ")
                                if escolhaConta.lower() == 's':
                                    break
                                else:
                                    for c in cliente.contas:
                                        if c.numero == escolhaConta:
                                            conta = c
                                    if conta == None:
                                        print("Conta não existe")
                                    else:
                                        while True:
                                            escolhaOperacoesConta = input(operacoesConta)
                                            if escolhaOperacoesConta == "1":
                                                    conta.verExtrato()
                                            elif escolhaOperacoesConta == "2":
                                                valor = float(input("Digite o valor: "))
                                                Saque(valor).registrar(conta)
                                            elif escolhaOperacoesConta == "3":                                       
                                                valor = float(input("Digite o valor: "))
                                                Deposito(valor).registrar(conta)
                                            elif escolhaOperacoesConta == "4":
                                                break
                        elif escolhaOperacoesCliente == "4":
                            break
    elif escolhaOpcoes == "4":
        break
    else: 
        print("Opção inválida")