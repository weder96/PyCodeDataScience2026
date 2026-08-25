'''
Herança - Um objeto é o outro objeto
'''


class Pessoa:

    def __init__(self, nome, cidade):

        self.nome = nome
        self.cidade = cidade

    def falar_sobre_futebol(self):

        print(f"{self.nome} está falando sobre futebol. (Vamos flamengo)")


class Investidor(Pessoa):

    def comprar_acoes(self):

        print(f"{self.nome} está comprando ações!")

class Politico(Pessoa):

    def fazer_leis(self):

        print(f"{self.nome} está fazendo leis")



brenno = Politico(nome = "Brenno", cidade = 'Niterói')

brenno.fazer_leis()

brenno.falar_sobre_futebol()























