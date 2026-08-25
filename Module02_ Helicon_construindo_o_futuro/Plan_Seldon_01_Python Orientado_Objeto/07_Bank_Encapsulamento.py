import time

class ContaBancaria:
    """
    Uma classe para simular uma conta bancária simples, demonstrando o uso de
    atributos públicos, protegidos e privados.
    """

    def __init__(self, titular, agencia, numero_conta, saldo_inicial=0.0):
        # ATRIBUTOS PÚBLICOS: Podem ser acessados e modificados livremente.
        self.titular = titular
        self.agencia = agencia
        self.numero_conta = numero_conta

        # ATRIBUTO PROTEGIDO (_): Uma convenção que diz "não mexa aqui fora da classe,
        # a menos que saiba o que está fazendo".
        self._ultima_operacao = None

        # ATRIBUTO PRIVADO (__): O Python renomeia este atributo internamente ("name mangling")
        # para dificultar (mas não impossibilitar) o acesso direto.
        # Ideal para dados críticos que não devem ser alterados sem passar por um método.
        self.__saldo = float(saldo_inicial)

    # MÉTODO PÚBLICO
    def depositar(self, valor):
        """
        Adiciona um valor ao saldo da conta.
        """
        if valor > 0:
            self.__saldo += valor
            self._registrar_operacao(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    # MÉTODO PÚBLICO
    def sacar(self, valor):
        """
        Retira um valor do saldo, se houver fundos suficientes.
        """
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
            return

        if self.__tem_fundos_suficientes(valor):
            self.__saldo -= valor
            self._registrar_operacao(f"Saque de R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação negada: Saldo insuficiente.")

    # MÉTODO PÚBLICO (GETTER)
    def ver_saldo(self):
        """
        Exibe o saldo atual da conta de forma segura.
        """
        print(f"O saldo atual da conta de {self.titular} é R$ {self.__saldo:.2f}")

    # MÉTODO PRIVADO
    def __tem_fundos_suficientes(self, valor):
        """
        Verifica internamente se o saldo permite o saque.
        Este método não deve ser chamado de fora da classe.
        """
        return self.__saldo >= valor

    # MÉTODO PROTEGIDO
    def _registrar_operacao(self, descricao_operacao):
        """
        Registra a data e hora da última operação.
        Protegido porque é um detalhe de implementação interno.
        """
        self._ultima_operacao = f"{descricao_operacao} em {time.ctime()}"

# --- Demonstração de Uso ---

print("Criando uma nova conta...")
minha_conta = ContaBancaria(titular="Weder Sousa", agencia="001", numero_conta="12345-6", saldo_inicial=1000)
minha_conta.ver_saldo()
print("-" * 30)

print("Realizando operações válidas...")
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.ver_saldo()
print("-" * 30)

print("Tentando um saque inválido...")
minha_conta.sacar(2000) # Vai falhar
minha_conta.ver_saldo() # Saldo continua o mesmo
print("-" * 30)


# --- Demonstração dos níveis de acesso ---
print("Tentando acessar e modificar os atributos...")

# 1. Atributo Público: Acesso e modificação permitidos.
print(f"Titular antigo: {minha_conta.titular}")
minha_conta.titular = "José da Silva"
print(f"Titular novo: {minha_conta.titular}")
print("\n")

# 2. Atributo Protegido: Acessível, mas a convenção diz para não fazer.
print(f"Última operação (protegido): {minha_conta._ultima_operacao}")
minha_conta._ultima_operacao = "Isso não deveria ser feito!" # Funciona, mas quebra a convenção.
print(f"Última operação modificada: {minha_conta._ultima_operacao}")
print("\n")


# 3. Atributo Privado: O acesso direto falha ou se comporta de forma inesperada.
print("Tentando modificar o saldo diretamente...")
minha_conta.__saldo = 9999999 # Isso NÃO altera o saldo real!
print(f"Atributo que acabamos de criar: {minha_conta.__saldo}")

print("Verificando o saldo real com o método correto:")
minha_conta.ver_saldo() # O método ver_saldo() ainda acessa o saldo real, que não foi alterado.
print("\n")

# A forma "correta" de acessar um atributo privado (que não deve ser usada na prática)
# é usando o nome "mutilado" que o Python cria.
print("Acessando o atributo 'privado' da forma que o Python enxerga:")
print(f"Saldo real via acesso especial: {minha_conta._ContaBancaria__saldo}")