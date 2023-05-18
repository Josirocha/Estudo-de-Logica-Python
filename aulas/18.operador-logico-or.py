# operadores lógicos
# and (e)  or (ou)  not (não)
# or -Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se o valor for considerado verdadeiro,
#a expressão inteira será avaliada naquele valor.
# São considerados falsy ( o que já vi)
# 0 0.0 '' False
# também existe o tipo None que é
# usado para representar um não valor
# entrada = input('[E]ntrar [S]air')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'
# #if True
# if(entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliaçao de curto circuito
# print(0 or False or 0 or 'abc' or True)
senha = input('Senha: ') or 'Sem senha'
print(senha)
