###################Prova###################
## Autor: Uriel Gonçalves Paiva da conceição
## Turma: FEAU-4UNA
## Matricula: 02010287
############################################# 
import numpy as np
from numpy import linalg
import time
import timeit
E = np.array([[9,-5,-2,-3],
              [-3,4,2,-7],
              [-6,0,4,8]], dtype='double')
if len(E[:,0]) == 3 and len(E[0,:])==4:
  print(E)
print("............................................")
A = np.delete(E, 3, axis=1)
print(A)
erro = float(input('Informe o valor do erro epsilon '))
n = int(input('Informe a quantidade de casas decimais do arredondamento da solução '))
X = [0,100]
X1= 100
Y = [0,100]
Y1 = 100
Z = [0,100]
Z1 = 100
i = 0
#X.append()
while ((abs(X[0] - X[1])>= erro) or (abs(Y[0] - Y[1])>= erro) or (abs(Z[0] - Z[1])>= erro)):
  if i > 0:
    X[0] = X[1]
    Y[0] = Y[1]
    Z[0] = Z[1]
  X[1] = (E[0,3]-E[0,1]*Y[0]-E[0,2]*Z[0])/E[0,0]
  Y[1] = (E[1,3]-E[1,0]*X[0]-E[1,2]*Z[0])/E[1,1]
  Z[1] = (E[2,3]-E[2,0]*X[0]-E[2,1]*Y[0])/E[2,2]
  i = i + 1
  if i == 2000:
    break
print('Sol mét Gauss-Jacobi é {0}, {1}, {2},com {3} iterações e erro = {4}'.format(round(X[1],n), round(Y[1],n), round(Z[1],n), i ,erro))