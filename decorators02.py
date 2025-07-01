import time


# decorator para medir tempo de execução

def medir_tempo(funcao):
    def wrapper (*args, **Kwargs):
        inicio = time.time()
        resultado = funcao(*args, **Kwargs)
        fim = time.time()
        print(f"A função '{funcao.__name__}' demorou {fim - inicio:.6f} segundos para ser executada.")
        return resultado

    return wrapper

@medir_tempo
def exemplo_funcao(tempo_espera):
    time.sleep(tempo_espera)
    print('A função foi executada')

exemplo_funcao(2)