"""
Enunciado do exercicio:
https://www.beecrowd.com.br/judge/pt/problems/view/1023
"""

import  random
moradores_por_casa = []
consumo_por_casa = []
media_consumo_por_casa = []
media_consumo_por_casa_crescente = []
moradores_por_casa_crescente = []

qtd_cidade = random.randint(1,1*10**6)
n_cidade = 0

"""
def cidade_funcao(x,y,z,i):
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

    while ( i < qtd_casas):
        print("Cidade {}"
            "\n P - C"
            "\n {} - {}".format(n_cidade,moradores_por_casa[media_consumo_por_casa.index(media_consumo_por_casa_crescente[i])],media_consumo_por_casa_crescente[i]))
        i+=1
"""

while (n_cidade < qtd_cidade):
    x=0
    y=0
    z=0
    i=0
    n=1
    moradores_por_casa.clear()
    consumo_por_casa.clear()
    media_consumo_por_casa.clear()
    media_consumo_por_casa_crescente.clear()
    moradores_por_casa_crescente.clear()
    qtd_casas=0
    qtd_casas = random.randint(1,10)

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

    print("Pessoas/casa - Consumo/pessoa")
    print("Cidade nº ",n_cidade+1)
    while ( i < qtd_casas):
        print("\n {} - {}".format(moradores_por_casa[media_consumo_por_casa.index(media_consumo_por_casa_crescente[i])],media_consumo_por_casa_crescente[i]))
        i+=1


    n_cidade+=1


"""
print("moradores_por_casa",moradores_por_casa)
print("consumo_por_casa",consumo_por_casa)
print("media_consumo_por_casa",media_consumo_por_casa)
print("media_consumo_por_casa_crescente",media_consumo_por_casa_crescente)
print("moradores_por_casa_crescente",moradores_por_casa_crescente)
print("*"*30)
"""






