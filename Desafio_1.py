# Função para receber dois dados do usuário e concatenar em uma string
def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    
    # Concatena os dados com um espaço entre eles
    string_concatenada = dado1 + " " + dado2
    
    return string_concatenada

# Chama a função e exibe o resultado
resultado = concatenar_dados()
print("String concatenada:", resultado)
