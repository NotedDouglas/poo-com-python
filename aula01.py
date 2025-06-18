import time
from turtledemo.penrose import start

import numpy

# Exemplo de criação:
# ndarray1 = numpy.zeros(100000)
# print(f' 1- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
# ndarray1 = numpy.ones(100000)
# print(f' 2 - Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
# ndarray1 = numpy.linspace(10, 1000, 1000)
# print(f' 3- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')


# Comparar desempenho
# start_time = time.time()
# lista = [0] * 1000000000
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos levou: {elapsed_time}')
#
# start_time = time.time()
# ndarray1 = numpy.zeros (1000000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos levou: {elapsed_time}')

# Dá para melhorar se definimos o tipo de dado, exemplo: dado tipo int (para valores de 0 -250)
# start_time = time.time()
# ndarray1 = numpy.zeros (1000000000, dtype='uint8')
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos em int de 8 não sinalizado levou: {elapsed_time}')
#
# # posso criar vetores, matrizes e tensores
# rng = numpy.random.default_rng() # numpy tem seus métodos random inclusos
# vetor = rng.random(4)
# print(f'Array de 1 Dimensão (VETOR) randômico:\n{vetor}\n')
# matriz = rng.random([4, 4])
# print(f'Array de 2 Dimensão (MATRIZ) randômico:\n{matriz}\n')
# tensor = rng.random([4, 4, 4])
# print(f'Array de 1 Dimensão (TENSOR) randômico: \n{tensor}\n')

#Prepara ndarrays  para serem representados por gráficos:
vetor_a = numpy.linspace(10, 1000, 100)
vetor_b = numpy.linspace(10, 3000, 100)
vetor_c =  numpy.linspace(10, 8000, 100)

print(vetor_a)
print(vetor_b)
print(vetor_c)

# Numpy tem métodos diretos de como salvar um arquivo no formato .txt
numpy.savetxt('vetor_a.txt', vetor_a, fmt='%f', delimiter=';')
numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')

# Utilizando biblioteca plotar gráfica
import plotly.express

array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')
print(array_a)

array_abc = numpy.vstack([array_a, array_b, array_c])
print(array_abc)
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()



