# Definir classe Cat e instanciar objeto no main
from collections.abc import async_generator


class Dog:
    def __init__(self):
        pass


rex = Dog()
print(rex)


# Inserir Atributo Valor Fixo

class Dog:
    def __init__(self):
        self.age = 5


rex = Dog()
print(f'A idade do rex é:  {rex.age}')
caramelo = Dog()
print(f'A idade do caramelo é:  {caramelo.age}')


# Atributo com passagem de parâmetros no construtor da class

class Dog:
    def __init__(self, age):
        self.age = age


rex = Dog(10)
print(f'A idade do rex é:  {rex.age}')
caramelo = Dog(5)
print(f'A idade do caramelo é:  {caramelo.age}')


# Atributo da classe

class Dog:
    family = 'Canidae'

    def __init__(self, age):
        self.age = age


rex = Dog(10)
print(f'A idade do rex é:  {rex.age} e pertence a família: {rex.family}')
caramelo = Dog(5)
print(f'A idade do Caramelo é:  {rex.age} e pertence a família: {rex.family}')

print(f'Todos os cachorros pertence a família: {Dog.family}')


# Definindo um tipo de atributo

class Dog:
    family = 'Canidae'

    def __init__(self, age: int):
        self.age: int = age


# Atribuindo __class__ e __name__

class Dog:
    family = 'Canidae'

    def __init__(self, age: int):
        self.age: int = age


print(f'Rex é um objeto de qual classe? R: {rex.__class__.__name__}')
print(f'Caramelo é um objeto de qual classe? R: {caramelo.__class__.__name__}')

# Herança

class Animal:
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        self.age = age
        self.height = height
        self.weight = weight
        self.position: tuple = position

    def move_x(self):
        self.position[0] += 1

    def move_y(self):
        self.position[1] += 1

    def move_z(self):
        self.position[2] += 2


class Dog(Animal):
    def __init__(self, age: int, height: int, weight: int, position: tuple):
        Animal.__init__(self, age, height, weight, position)

    def move_z(self):
        self.position[2] += 2


caramelo = Dog(10, 40, 30, (0, 0, 0))
print(caramelo.age, caramelo.weight)
