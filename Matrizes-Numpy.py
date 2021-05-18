#Exercicio 1 - Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'Hum','Dois']. 
#A ideia do exercício é tirar a média de todos os valores contidos na lista, 
#porém para fazer o cálculo precisa remover as strings.

soma = 0
lista_numeros = [6,7,4,7,8,4,2,5,7,'hum','dois']
elementos = len(lista_numeros)
lista_numeros.remove('hum')
lista_numeros.remove('dois')

for ex in lista_numeros:
  print(ex,'', end='')
  soma=soma+ex
print('')
print('')
print('Resultado da soma')
print(soma)
print('Média')
print(soma/elementos)


#Exercicio 2 - crie um método que receba duas matrizes, some os valores total de
#cada matriz e depois multiple o resultado delas e retorne o valor.

matr1 = [[2,5,6],[3,5,2]]
matr2 = [[6,7,2],[4,7,1]]
print('Matriz A= ',  matr1)
print('Matriz B= ', matr2)
print('')
def var(matr1,matr2):
  resultado=0
  resultado1=0
  for l1 in matr1:
    for c1 in l1:
       resultado=c1+resultado
  print('Resultado matriz A = ', resultado)
  for l2 in matr2:
    for c2 in l2:
      resultado1=c2+resultado1 
  print('Resultado matriz B = ', resultado1)  
  print(resultado*resultado1) 

var(matr1,matr2)


import numpy as np

#3. Criar uma matriz nxm (n = 5, m =7)
#a. faça a matriz transposta desta matriz
#b. somar toda matrix
#c. somar todas as colunas
#d. somar todas as linhas.
#e. retorne o maior valor
#f. retorne o menor valor.

#3
matriz = np.arange(35).reshape(5,7)
matriz

#a
matriz.T

#b
matriz.sum()

#c
matriz.sum(axis=0)

#d
matriz.sum(axis=1)

#e
matriz.max()

#f
matriz.min()


#Exercicio 5 - crie um array de números que vai de 0 a 1000.
a = np.arange(1001)
a


#Exercicio 6 - crie uma matriz só de zeros.

b = np.zeros((5,5), dtype=np.float64)

b
