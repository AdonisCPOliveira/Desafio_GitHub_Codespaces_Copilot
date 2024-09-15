# Função para receber uma string e um número inteiro do usuário
def repetir_string():
    string = input("Digite uma string: ")
    numero = int(input("Digite um número inteiro: "))
    
    # Repete a string o número de vezes informado
    string_repetida = string * numero
    
    return string_repetida

# Chama a função e exibe o resultado
resultado = repetir_string()
print("String repetida:", resultado)
