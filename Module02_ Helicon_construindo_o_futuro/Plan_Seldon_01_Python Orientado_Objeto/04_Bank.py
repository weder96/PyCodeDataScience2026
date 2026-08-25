
class Bank:

    ano_atual = 2022
    

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




    #4: Método de classe

    #é referente a classe, não a instancia (objeto específico). 
    #Pode ser usado para construir as instancias, quando você só tem parte dos argumentos necessários.
    #vamos supor que você precisa do ano de fundação mas só tem os anos de existencia da bank. 
    #Você pode construir um método de classe q calcula isso pra você.

     #atributo de classe. Não importa a instância
    
    @classmethod 
    def extraindo_bank_por_ano_existencia(cls, anos_existencia, nome, ticker, cnpj):

        ano_fundacao = cls.ano_atual - anos_existencia
        return cls(nome, ticker, ano_fundacao, cnpj) #tem que ser na mesma ordem do init

        #usado pra quando voce nao tem, ou não quer ter a instancia no primeiro momento

    @classmethod
    def extraindo_bank_corrigindo_ticker(cls, nome, texto_ticker, codigo_ticker, ano_fundacao, cnpj): 

        ticker = texto_ticker + codigo_ticker
        return cls(nome, ticker, ano_fundacao, cnpj)

if __name__ == "__main__": 


    itau = Bank.extraindo_bank_por_ano_existencia(nome = "Itau", ticker = "ITAU3", anos_existencia=62, cnpj="84.429.695/0001-11")


    print(itau.ano_fundacao)


    itau = Bank.extraindo_bank_corrigindo_ticker(nome = "ITAU", texto_ticker = "ITAUE", codigo_ticker = "3",
                                                                            ano_fundacao=1960, cnpj="84.429.695/0001-11")

    print(itau.ticker)





#Ex 113: Elabore um método de classe que você crie uma instância a partir das informações
#  nome, texto_ticker, codigo_ticker, ano_fundacao e cnpj. Você irá passar os argumentos "ITAUE" e "3", por exemplo, a, partir disso, será
#criado o atributo ticker. 
                                                                            



