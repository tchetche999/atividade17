# Exercício Python 17: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
ano_nascimento = int(input("Informe o ano de nascimento: "))
import datetime
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento
if idade < 18:
    anos_restantes = 18 - idade
    print(f"Você tem {idade} anos e precisa se alistar daqui a {anos_restantes} anos.")
elif idade == 18:
    print("Você tem 18 anos e está na hora de se alistar no serviço militar.")
else:
    anos_passados = idade - 18
    print(f"Você tem {idade} anos e já passaram {anos_passados} anos do prazo de alistamento.")