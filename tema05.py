class Casa:
    def __init__(self, num_quartos=None, num_banheiros=None, tem_garagem=False, tem_jardim=False):
        self.num_quartos = num_quartos
        self.num_banheiros = num_banheiros
        self.tem_garagem = tem_garagem
        self.tem_jardim = tem_jardim


    def __str__(self):
        caracteristicas = []
        if self.num_quartos:
            caracteristicas.append(f'Números de quartos: {self.num_quartos}')
        if self.num_banheiros:
            caracteristicas.append(f'Número de banheiros: {self.num_banheiros}')
        if self.tem_garagem:
            caracteristicas.append('Possui garagem: ')
        if self.tem_jardim:
            caracteristicas.append('Possui jardim: ')

        return ', '.join(caracteristicas)

# Construindo uma casa com garagem e jardim
casa = Casa(num_quartos=3, num_banheiros=2, tem_garagem=True, tem_jardim=False)
print('Características da Casa: ', casa)

# Outra casa
outra_casa = Casa (num_quartos=4, num_banheiros=3)


# Agora com Builder
class Casa:
    def __init__(self): #Contrutor vazio
        self.num_quartos = None
        self.num_banheiros = None
        self.tem_garagem = False
        self.tem_jardim = False


    def __str__(self):
        caracteristicas = []
        if self.num_quartos:
            caracteristicas.append(f'Números de quartos: {self.num_quartos}')
        if self.num_banheiros:
            caracteristicas.append(f'Número de banheiros: {self.num_banheiros}')
        if self.tem_garagem:
            caracteristicas.append('Possui garagem')
        if self.tem_jardim:
            caracteristicas.append('Possui jardim')

        return ', '.join(caracteristicas)

# Classe builder para construir a casa passo a passo

class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def set_num_quartos(self, num_quartos):
        self.casa.num_quartos = num_quartos
        return self

    def set_num_banheiros(self, num_banheiros):
        self.casa.num_banheiros = num_banheiros
        return self

    def adicionar_garagem(self):
        self.casa.tem_garagem = True
        return self

    def adicionar_jardim(self):
        self.casa.tem_jardim = True
        return self

    def obter_cas(self):
        return self.casa

#Construindo casa com garagem e jardim
builder_casa = CasaBuilder()
casa = builder_casa.set_num_quartos(3).set_num_banheiros(2).adicionar_garagem().adicionar_jardim().obter_cas()
print('Características da Casa: ', casa)
