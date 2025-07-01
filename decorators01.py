def meu_decorator(funcao):
    def wrapper():
        print('A função será executada agora.')
        funcao()
        print('A função foi executada.')

    return wrapper

# Aplicando o decorator usando o @

@meu_decorator
def minha_funcao():
    print('Esta é a função original')

# Chamado da função decorada
minha_funcao()