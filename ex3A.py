import json

with open('faturamento.json') as f:
   data = json.load(f)

valores_list = data.values()

lista_ignorando = [x for x in valores_list if x >= 1]

menor_valor = min(lista_ignorando)

maior_valor = max(lista_ignorando)

media = sum(lista_ignorando)/len(lista_ignorando)

maior_que_media = len([i for i in lista_ignorando if i > media]) 

print(f'Menor Valor: {menor_valor}\n')
print(f'Maior Valor: {maior_valor}\n')
print(f'Valores > Media: {maior_que_media}\n')