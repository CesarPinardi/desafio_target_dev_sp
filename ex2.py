prim_num = [0, 1]  # se inicia por 0 e 1

input= int(input('Numero a ser verificado: \n'))

while prim_num[-1] <= input: #faz fibonacci até o termo
    prim_num.append(prim_num[-1] + prim_num[-2])

if input in prim_num: # se o input tiver na lista 
    print('Faz parte de fibonacci')
else:
    print('Nao faz parte de fibonacci')