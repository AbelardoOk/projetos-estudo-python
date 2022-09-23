# Gerador aleatório de histórias

import random

comeco = ['Há 100 anos atrás', 'Nos anos 90', 'Há muito tempo atrás']
personagem = [' Afonso', ' João', ' Danilo']
dev = [' comeu uma maçã', ' matou um ganso', ' Foi atacado por um pitelopiteco']
final = [' e passou mal', ' e depois ficou feliz', ' e foi diagnosticado com COVID-19']

print(random.choice(comeco)+random.choice(personagem)+
      random.choice(dev)+random.choice(final))
