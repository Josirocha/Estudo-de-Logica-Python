# operadores lógicos
# and (e)  or (ou)  not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy ( o que já vi)
# 0 0.0 '' False
# também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar [S]air')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'
# #if True
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')
# Avaliaçao de curto circuito
print(True and False and True) #False
print(bool('')) #False

