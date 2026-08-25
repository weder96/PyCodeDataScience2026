

class Empresa:

    def __init__(self, nome, ticker, ano_fundacao, cnpj): #construtor

        self.nome = nome #atributos da instancia 
        self.ticker = ticker
        
        self.ano_fundacao = ano_fundacao
        self.cnpj = cnpj


class Carro:

    def __init__(self, cor, direcao): 

        self.cor_do_carro = cor 
        self.tipo_direcao = direcao


if __name__ == "__main__": #isso aqui serve para fazer testes dentro do próprio código. Só vai rodar quando rodar esse código como main

    empresa_de_motor = Empresa(nome = "Itau", ticker = "ITAB3", ano_fundacao = 1960, cnpj = "3981381291")
    carro_do_nelson = Carro(cor = "Preta", direcao = "Elétrica")

    print(empresa_de_motor.ano_fundacao)
    print(carro_do_nelson.cor_do_carro)
        





























