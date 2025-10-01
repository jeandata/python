CONSTANTE_BONUS = 1000

nome = input(("Digite seu nome:"))

salario = float(input("Digite o valor de seu salario:"))

bonus = float(input("Digite o valor de seu bonus:"))

valor_final = CONSTANTE_BONUS + salario * bonus
print(f"{nome}, o valor final de seu salario junto com o bonus é: R${valor_final}")
