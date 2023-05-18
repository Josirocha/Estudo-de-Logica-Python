#Operadores in e not in
#estar entre e não esta entre
# Strings são iteráveis - navegar item por item
# 0 1 2 3 4 5 6 
# J O S I A N E
# -7-6-5-4-3-2-1

# nome = 'Josiane'
# print(nome[4])
# print(nome[-3])

# print('a' in nome)
# print('u' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não está em {nome}')