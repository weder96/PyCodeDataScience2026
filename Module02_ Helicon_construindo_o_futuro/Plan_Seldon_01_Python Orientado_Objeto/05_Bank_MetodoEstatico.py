import random

class Bank:

    ano_atual = 2022 #atributo de classe. Não importa a instância

    def __init__(self, nome, ticker, ano_fundacao, cnpj): #construtor
        self.nome = nome #atributos da instancia 
        self.ticker = ticker
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj

    def tempo_existencia(self): 
    #preciso passar o self pois é um método da instancia. Só é possível executar ele com os atributos da instancia existindo

        self.anos_existencia = self.ano_atual - self.ano_fundacao
        print(f"A bank existe há {self.anos_existencia} anos!")

    def cnpj_numerico(self): 

        self.cnpj_inteiro = int(self.cnpj.replace("-", "").replace(".", "").replace("/", ""))
        print(f"O CNPJ só com números é {self.cnpj_inteiro}.")

    @classmethod #é referente a classe, não a instancia. Pode ser usado para construir a instancias, quando você só tem parte dos argumentos necessários.
    #vamos supor que você precisa do ano de fundação mas só tem os anos de existencia da bank. Você pode construir um método de classe q calcula isso pra você.
    def extraindo_bank_por_ano_existencia(cls, anos_existencia, nome, ticker, cnpj):

        ano_fundacao = cls.ano_atual - anos_existencia
        return cls(nome, ticker, ano_fundacao, cnpj) #tem que ser na mesma ordem do init

        #usado pra quando voce nao tem, ou não quer ter a instancia no primeiro momento
    
    @classmethod
    def extraindo_bank_corrigindo_ticker(cls, nome, texto_ticker, codigo_ticker, ano_fundacao, cnpj): 

        ticker = texto_ticker + codigo_ticker
        return cls(nome, ticker, ano_fundacao, cnpj)

    @staticmethod #só deixa aqui por organização, uma função normal
    def gera_id():

        id_aleatorio = random.randint(0, 100)
        return id_aleatorio

    @staticmethod
    def gera_recomendacao_investimento(ticker):

        lista_recomendacoes = ['Itau', 'Santader', 'Bradesco']
        recomendacao = random.choice(lista_recomendacoes)

        return print(f"A recomendação é de {recomendacao} para a bank {ticker}")


if __name__ == "__main__": 


    id_bank = Bank.gera_id()

    #print(id_bank)

    bank_recomendada = Bank.gera_recomendacao_investimento("1960")



