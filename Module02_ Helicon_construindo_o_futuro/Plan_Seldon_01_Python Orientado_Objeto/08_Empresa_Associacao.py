

'''
Associação - Uma classe usa a outra, mas existem sozinhas

Classe dados x banco de dados.

'''


class Cotacoes_empresas:

    def __init__(self):

        self.cotacoes = [20, 20.03, 21, 22.30]
        #self.bd = Banco_de_dados(user = "edufinance", senha = "codigo python")

    def soma_cotacoes(self):

        return print(sum(self.cotacoes))
    
    def colocar_cotacoes_na_base_de_dados(self):

        self.bd.iniciar_conexao()

        colocar_dados = (self.bd.conexao, self.cotacoes)

        print("Dados na base!")




# class Banco_de_dados:

#     def __init__(self, senha, user):

#         self.senha = senha
#         self.user = user

#     def iniciar_conexao(self):

#         self.conexao = self.user + self.senha

#         print('Conexão iniciada com sucesso')


teste_cotacoes = Cotacoes_empresas()

teste_cotacoes.soma_cotacoes()


# teste_banco = Banco_de_dados(user = "edufinance", senha = "codigo python")

# teste_banco.iniciar_conexao()







