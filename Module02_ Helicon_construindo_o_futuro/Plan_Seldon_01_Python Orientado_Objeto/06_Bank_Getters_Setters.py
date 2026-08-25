import random
from datetime import datetime

class ContaBancaria:

    # Atributo de classe. É o mesmo para qualquer instância (conta) criada.
    ano_atual = datetime.now().year 

    def __init__(self, titular, numero_conta, ano_abertura, cpf): # Construtor
        
        # O __ torna o atributo "privado", dificultando o acesso direto de fora da classe.
        self._titular = titular 
        
        # Atributos da instância
        self.numero_conta = numero_conta
        self.ano_abertura = ano_abertura # Este será controlado pelo getter/setter
        self.cpf = cpf

    def tempo_de_conta(self): 
        # Precisa do "self" pois é um método da instância.
        # Ele usa os atributos específicos desta conta.
        self.anos_de_conta = self.ano_atual - self.ano_abertura
        print(f"Esta conta existe há {self.anos_de_conta} anos!")

    def cpf_numerico(self): 
        # Remove a formatação do CPF para obter apenas os números.
        self.cpf_inteiro = int(self.cpf.replace("-", "").replace(".", ""))
        print(f"O CPF só com números é {self.cpf_inteiro}.")

    @classmethod # É referente à classe, não a uma instância específica.
    # Pode ser usado para criar instâncias de formas alternativas.
    # Ex: Criar uma conta a partir do tempo que o cliente já tem, e não do ano de abertura.
    def abrir_conta_por_tempo_cliente(cls, anos_de_conta, titular, numero_conta, cpf):
        ano_abertura = cls.ano_atual - anos_de_conta
        # Retorna uma nova instância da classe, chamando o __init__ com os dados calculados.
        return cls(titular, numero_conta, ano_abertura, cpf)

    @classmethod
    def abrir_conta_formatando_numero(cls, titular, agencia, numero_base, digito, ano_abertura, cpf): 
        # Outro método de fábrica: cria a conta a partir de partes do número.
        numero_conta_completo = f"{agencia}-{numero_base}-{digito}"
        return cls(titular, numero_conta_completo, ano_abertura, cpf)

    @staticmethod # Uma função normal que fica dentro da classe por organização.
    # Não acessa nem a classe (cls) nem a instância (self).
    def gera_id_atendimento():
        id_aleatorio = random.randint(1000, 9999)
        return id_aleatorio
    
    @staticmethod
    def gera_sugestao_credito(): 
        # Função utilitária relacionada ao "banco", mas não a uma conta específica.
        lista_sugestoes = ['Crédito Aprovado', 'Análise Pendente', 'Crédito Negado']
        sugestao = random.choice(lista_sugestoes)
        return print(sugestao)

    # Getter e Setter servem para tratar/validar dados no momento em que são definidos ou acessados.
    # Evita a necessidade de tratar o dado em vários lugares diferentes na classe.
    # Funciona como um validador de dados.

    # GETTER para ano_abertura
    @property
    def ano_abertura(self):
        # Quando você acessa `conta.ano_abertura`, este método é chamado.
        return self._ano_abertura

    # SETTER para ano_abertura
    @ano_abertura.setter
    def ano_abertura(self, ano):
        # Quando você define `conta.ano_abertura = 2020`, este método é chamado.
        # Aqui garantimos que o ano seja sempre um número inteiro.
        self._ano_abertura = int(ano)


    @property 
    def titular(self): 
        # Quando você acessa `conta.titular`, este método é executado.
        return self._titular
    
    @titular.setter 
    def titular(self, nome): 
        # Quando você define `conta.titular = "nome"`, este método é executado.
        # Ele garante que o nome seja sempre salvo no formato Title Case.
        self._titular = nome.title()


if __name__ == "__main__": 

    # Criando uma instância. Note que o nome "weder sousa" está em minúsculas.
    conta_itau = ContaBancaria(titular="weder sousa", numero_conta="12345-6", ano_abertura="2018", cpf="123.456.789-00")

    # Ao imprimir, o getter é chamado e o setter já formatou o nome para Title Case.
    print("Titular (após formatação do setter): ", {conta_itau.titular})
    print("Número da conta: ", {conta_itau.numero_conta})
    print("-" * 30)

    # Exemplo do método de instância
    conta_itau.tempo_de_conta()
    print("-" * 30)
    
    # Exemplo do método estático
    print(f"ID de Atendimento gerado: {ContaBancaria.gera_id_atendimento()}")
    ContaBancaria.gera_sugestao_credito()
    print("-" * 30)

    # Exemplo do método de classe
    conta_nubank = ContaBancaria.abrir_conta_por_tempo_cliente(2, "Maria Silva", "7890-1", "987.654.321-99")
    print(f"Conta criada com método de classe:")
    print(f"Titular: {conta_nubank.titular}, Ano de Abertura: {conta_nubank.ano_abertura}")