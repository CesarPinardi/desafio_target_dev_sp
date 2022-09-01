import json
from collections import Counter

with open('dados.json') as f:
   data = json.load(f)

valores_list = data

my_dict = Counter()

for d in valores_list:
    for key, value in d.items():
        my_dict[key] += value

total = my_dict['valor']

tam = len(valores_list)

media = total/tam

seq = [x['valor'] for x in valores_list]

menor_valor = min(seq)
maior_valor = max(seq)

print(f'Menor Valor: {menor_valor}\n')
print(f'Maior Valor: {maior_valor}\n')
print(f'Valores > Media: {media}\n')


