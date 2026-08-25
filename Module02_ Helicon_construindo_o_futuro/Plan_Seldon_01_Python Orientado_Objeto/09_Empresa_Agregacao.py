
'''
Agregação -> A classe usa outra classe mas ela precisa da outra pra existir. 
Elas existem sozinhas mas precisam funcionar juntas.
Ações + Carteira de investimento
'''

class Carteira_investimento:

    def __init__(self, nome_pessoa):

        self.proprietario = nome_pessoa
        self.carteira = []

    def inserir_acao(self, acao):

        self.carteira.append(acao)

    def listar_acoes(self):

        for acao in self.carteira:

            print(acao.ticker, acao.nome_empresa)

class Acoes:

    def __init__(self, ticker, nome_empresa):

        self.ticker = ticker
        self.nome_empresa = nome_empresa


#um carro e uma roda existem sozinhos, mas um carro sem roda é meio estranho

carteira_brenno = Carteira_investimento("Brenno")

weg = Acoes("WEGE3", "Weg")
petro = Acoes("PETR4", "Petrobras")

carteira_brenno.inserir_acao(weg)
carteira_brenno.inserir_acao(petro)

carteira_brenno.listar_acoes()






