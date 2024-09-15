# Função para receber dois números e realizar as operações básicas
def operacoes_basicas():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2 if numero2 != 0 else "Divisão por zero não permitida"
    
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

# Chama a função para realizar as operações
operacoes_basicas()
