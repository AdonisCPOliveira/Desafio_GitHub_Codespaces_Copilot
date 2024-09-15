
# Exemplos de Programas em Python

Este repositório contém exemplos simples de programas em Python que realizam diferentes tarefas de manipulação de dados recebidos do usuário.

## Exemplo 1: Concatenar dois dados

**Descrição:**
Este programa recebe dois dados diferentes do usuário (dois textos) e concatena-os em uma única string, separada por um espaço.

```python
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
```

## Exemplo 2: Repetir uma string com base em um número inteiro

**Descrição:**
Este programa recebe uma string e um número inteiro. A string será repetida o número de vezes equivalente ao número inteiro informado.

```python
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
```

## Exemplo 3: Realizar quatro operações básicas

**Descrição:**
Este programa recebe dois números do usuário e realiza as quatro operações matemáticas básicas: soma, subtração, multiplicação e divisão. Se o divisor for 0, o programa exibe uma mensagem apropriada para evitar a divisão por zero.

```python
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
```

##Exemplo 4: Verificar se um número é par ou ímpar

**Descrição:**
Este programa solicita que o usuário insira um número inteiro e verifica se o número é par ou ímpar.

```python
# Função para verificar se um número é par ou ímpar
def verificar_par_impar():
    numero = int(input("Digite um número inteiro: "))
    
    if numero % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")

# Chama a função
verificar_par_impar()
```

##Exemplo 5: Calcular a média de três números

**Descrição:**
Este programa recebe três números do usuário, calcula e exibe a média aritmética desses números.

```python
# Função para calcular a média de três números
def calcular_media():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    numero3 = float(input("Digite o terceiro número: "))
    
    media = (numero1 + numero2 + numero3) / 3
    print(f"A média dos números é: {media}")

# Chama a função
calcular_media()
```

## Como executar os códigos

1. Faça o clone do repositório ou baixe os arquivos individualmente.
2. Execute o código em um ambiente Python (pode ser localmente ou via IDE como PyCharm, VSCode, etc).
3. Siga as instruções que aparecem no terminal para inserir os dados e ver os resultados.
