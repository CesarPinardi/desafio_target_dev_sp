faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

estados = ['SP', 'RJ', 'MG', 'ES', 'Outros']


valores_list = faturamento_mensal.values()

valores_keys = faturamento_mensal.keys()

fat_total = sum(valores_list)

print(f'Faturamento total: R${fat_total}')

cont = 0

for i in valores_list:
    cont += 1
    percentual = ((i / fat_total) * 100)
    print(f'Percentual de {estados[cont-1]} é: {percentual:.1f}%')