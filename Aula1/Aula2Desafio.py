CONSTANTE_BONUS = 1000

def nome_usuario():
    try:
        nome = str(input("Digite seu nome: "))
        return nome
    except Exception as e:
        print(f"Erro ao obter nome: {e}")

def salario():
    try:
        salario = float(input("Digite o valor de seu salario: "))
        return salario
    except Exception as e:
        print(f"Erro ao obter salario: {e}")

def bonus_do_salario():
    try:
        bonus = float(input("Digite o valor de seu bonus: "))
        return bonus
    except Exception as e:
        print(f"Erro ao obter bonus: {e}")

def conta(salario, bonus, valor_final):
    valor_final = CONSTANTE_BONUS + salario * bonus
    return valor_final

nome_usuario = nome_usuario()
print(nome_usuario)