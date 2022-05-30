"""
Enunciado do exercicio:
https://www.beecrowd.com.br/judge/pt/problems/view/1023
"""

import  random

qtd_casas = int(input("Digite a quantidade de casas: "))
x=0
y=0
z=0
i=0
moradores_por_casa = []
consumo_por_casa = []
media_consumo_por_casa = []
media_consumo_por_casa_crescente = []
moradores_por_casa_crescente = []


while (x < qtd_casas):
    n = random.randint(1,10)
    moradores_por_casa.append(n)
    moradores_por_casa_crescente.append(n)
    x+=1


while (y < qtd_casas):
    consumo_por_casa.append(moradores_por_casa[y] * random.randint(1,20))
    y+=1



while (z < qtd_casas):
    media_consumo_por_casa.append(consumo_por_casa[z]//moradores_por_casa[z])
    media_consumo_por_casa_crescente.append(consumo_por_casa[z]//moradores_por_casa[z])
    z+=1


media_consumo_por_casa_crescente.sort()
moradores_por_casa_crescente.sort()


print("moradores_por_casa",moradores_por_casa)
print("consumo_por_casa",consumo_por_casa)
print("media_consumo_por_casa",media_consumo_por_casa)
print("media_consumo_por_casa_crescente",media_consumo_por_casa_crescente)
print("moradores_por_casa_crescente",moradores_por_casa_crescente)
print("*"*30)

while ( i < qtd_casas):
    print("{} {}".format(moradores_por_casa[media_consumo_por_casa.index(media_consumo_por_casa_crescente[i])],media_consumo_por_casa_crescente[i]))
    i+=1

