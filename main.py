# # #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
sum1 = input("Digite um número inteiro: ")
sum2 = input("Digite outro número inteiro: ")

resultado = int(sum1) + int(sum2)
print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número: "))
print(num % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
mult1 = input("Digite um número inteiro: ")
mult2 = input("Digite outro número inteiro: ")

resultado = int(mult1) * int(mult2)
print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
div1 = int(input("Digite um número inteiro: "))
div2 = int(input("Digite outro número inteiro: "))

print(div1 // div2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
quad1 = int(input("Digite um número: "))

print(quad1 ** 2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input("Digite um número flutuante: "))
num2 = float(input("Digite outro número flutuante: "))

print(num1 + num2)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num3 = float(input("Digite um número flutuante: "))
num4 = float(input("Digite outro número flutuante: "))

media = (num3 + num4) / 2
print(f'A média é {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(base ** expoente)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f'{celsius}° Celsius é igual a {fahrenheit}° Fahrenheit.')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))

area = 3.14159 * (raio ** 2)

print(f'A área do círculo com raio {raio} é {area:.2f}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = input("Digite uma frase ou uma palavra: ")
print(palavra.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")
print(nome_completo.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/yyyy: ")
dia, mes, ano = data.split("/")
print("Dia: ", dia)
print("Mês: ", mes)
print("Ano: ", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite outra palavra: ")

print(palavra1 + " " + palavra2)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = True
expressao2 = False

print(expressao1 and expressao2)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
resultado_or = expressao1 or expressao2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resultado_not = not expressao1
print(resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
val1 = int(input("Digite um número: "))
val2 = int(input("Digite outro número: "))

print(val1 == val2)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print(val1 != val2)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}° Celsius é igual a {fahrenheit}° Fahrenheit.')
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
entrada = input("Digite uma palavra ou frase: ")

if entrada.isalpha(): 
    formatado = entrada.replace(" ", "").lower()  
    if formatado == formatado[::-1]: 
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite apenas letras.")

# 23: Calculadora Simples
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")

# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")