'''

Composição -> uma classe é dona de outra classe. Uma só existe se a outra existir. 
Se a classe principal for apagada, tudo é apagado. 

'''


class Empresa:

    def __init__(self, nome_empresa, ticker):

        self.nome = nome_empresa
        self.ticker = ticker
        self.enderecos = [] #Empresa pode ter varios endereços

    def adicionando_enderecos(self, estado, cidade, pais):

        self.enderecos.append(Endereco(estado, cidade, pais)) #diferente do código anterior, aqui a gente cria a classe dentro da outra classe

    def lista_enderecos(self):

        for endereco in self.enderecos:

            print(endereco.estado, endereco.cidade, endereco.pais)

    def __del__(self): #toda vez que o programa acaba, o python deleta itens 

        print(f"{self.nome} foi apagado")


class Endereco:

    def __init__(self, estado, cidade, pais):

        self.estado = estado
        self.cidade = cidade
        self.pais = pais

    def __del__(self): #toda vez que o programa acaba, o python deleta itens 

        print(f"{self.cidade} foi apagado")


weg = Empresa("Weg", "WEGE3")

weg.adicionando_enderecos(estado = 'SC', cidade = "Jaraguá do Sul", pais = "Brasil")
weg.adicionando_enderecos(estado = 'Missouri', cidade= 'Washington', pais = "EUA")

weg.lista_enderecos()

print("-" * 20)





