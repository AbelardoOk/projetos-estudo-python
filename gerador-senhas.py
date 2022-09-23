# Gerador aleatório de senhas

import random
import string

print("Olá, Bem vindo ao Gerador de Senhas")

largura = int(input('\nInsira o tamanho da senha: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits

todos = lower + upper + num
temp = random.sample(todos,largura)
senha = "".join(temp)

print(senha)
