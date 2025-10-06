# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# n1 = int(input("Primeiro numero: "))
# n2 = int(input("Segundo Numero: "))
# soma = n1 + n2
# print("A soma é: ", soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# n1 = float(input("Numero: "))
# valor_final = n1 % 5
# print(valor_final)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# n1 = int(input("Primeiro numero: "))
# n2 = int(input("Segundo Numero: "))
# valor_multiplicado = n1 * n2
# print(valor_multiplicado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# n1 = int(input("Primeiro numero: "))
# n2 = int(input("Segundo Numero: "))
# valor_divisao = n1/n2
# print(f"{valor_divisao:.0f}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# n1 = int(input("Primeiro numero: "))
# numero_quadrado = n1 ** 2
# print(numero_quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# n1 = float(input("Numero 1: "))
# n2 = float(input("Numero 2: "))
# valor_final = n1+n2
# print(valor_final)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# n1 = float(input("Numero 1: "))
# n2 = float(input("Numero 2: "))
# n3 = (n1+n2)/2
# print(n3)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# n1 = float(input("Numero: "))
# n2 = float(input("Expoente: "))
# n3 = n1 ** n2
# print(n3)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# n1 = float(input("Celsius: "))
# n2 = n1 * 1.8 + 32
# print(n2, "F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# n1 = float(input("Raio: "))
# n2 = 3.14 * (n1 ** 2)
# print(n2)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# nome = input("Nome: ").upper()
# print(nome)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Nome: ").lower()
# print(nome)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Frase: ").strip()
# print(frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite a data com /: ").split("/")
# print(f"Ano: {data[2]}, Mes: {data[1]}, Dia: {data[0]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# nome1= input("Palavra1: ")
# nome2= input("Palavra2: ")
# juncao = nome1 + nome2
# print(juncao)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# n1 = bool(input("Voce eh homem? "))
# n2 = bool(input("Voce eh maior de idade? "))
# n3 = n1 and n2
# print(n3)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# n1 = bool(input("Voce eh homem? "))
# n2 = bool(input("Voce eh maior de idade? "))
# n3 = n1 or n2
# print(n3)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# n1 = bool(input("Voce eh homem? "))
# n2 = not n1
# print(n2)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# n1 = int(input("Primeiro numero: "))
# n2 = int(input("Segundo numero: "))
# n3 = n1 == n2
# print(n3)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# n1 = int(input("Primeiro numero: "))
# n2 = int(input("Segundo numero: "))
# n3 = n1 != n2
# print(n3)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    n1 = float(input("Celsius: "))
    n2 = n1 * 1.8 + 32
    print(n2, "F")
except ValueError as e:
    print("Erro de valor inserido")

# 22: Verificador de Palíndromo

# 23: Calculadora Simples
try:
    print("Menu")
    print("1- Soma")
    print("2- Subtracao")
    print("3- Multiplicacao")
    print("4- Divisao")
    print("0 - Sair")
    menu = int(input("Digite o numero do tipo de equacao"))
    if menu == 1:
        n1 = float(input("Digite seu primeiro numero"))
        n2 = float(input("Digite seu segundo numero"))
        n3 = n1 + n2
    elif menu == 2:
        n1 = float(input("Digite seu primeiro numero"))
        n2 = float(input("Digite seu segundo numero"))
        if n1 > n2:
            n3 = n1 - n2
        else:
            n3 = n2 - n1
    elif menu == 3:
        n1 = float(input("Digite seu primeiro numero"))
        n2 = float(input("Digite seu segundo numero"))
        n3 = n1 * n2
    elif menu == 4:
        try:
            n1 = float(input("Digite seu primeiro numero"))
            n2 = float(input("Digite seu segundo numero"))
            n3 = n1 // n2
        except ZeroDivisionError as e:
            print("Divisao por 0 nao pode acontecer!!")
    else:
        exit()

except ValueError as e:
    print("Digite um numero!!")
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
