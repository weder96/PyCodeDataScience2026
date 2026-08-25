from datetime import datetime


class Bank:

    def __init__(self, nome, ticker, ano_fundacao, cnpj): #construtor

        self.nome = nome #atributos da instancia 
        self.ticker = ticker
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj
        self.ano_atual = datetime.now().year

    def tempo_existencia(self): 
    #preciso passar o self pois é um método da instancia. Só é possível executar ele com os atributos da instancia existindo

        self.anos_existencia = self.ano_atual - self.ano_fundacao
        print(f"A bank existe há {self.anos_existencia} anos!")

    def cnpj_numerico(self): 

        self.cnpj_inteiro = int(self.cnpj.replace("-", "").replace(".", "").replace("/", ""))
        print(f"O CNPJ só com números é {self.cnpj_inteiro}.")



if __name__ == "__main__": 


    itau = Bank(nome = "ITAU", ticker = "ITAUE3", ano_fundacao=1960, cnpj="84.429.695/0001-11")
    itau.cnpj_numerico()

    santader = Bank(nome = "Santader", ticker = "SANB3", ano_fundacao=1960, cnpj="90.400.888/0001-42")
    santader.cnpj_numerico()

    





















