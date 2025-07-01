class Carro:
    def __init__(self, classe_decorada):
        self.classe_decorada = classe_decorada

    def __call__(self, *args, **kwargs):
        # Instancia classe original
        instancia_classe = self.classe_decorada(*args, **kwargs)
        # Adicionar atributo
        instancia_classe.num_rodas = 4
        return instancia_classe

@Carro
class Automovel:
    def __init__(self, modelo):
        self.modelo = modelo

# Criando instancia da classe decorada
new_auto = Automovel('Gol')


print(new_auto.modelo)
print(new_auto.num_rodas)