###################Projeto#####################################
## Grupo Autor: Fênix
## Integrantes: Uriel Paiva, Felipe Franco, Paloma Machado
##############################################################
L=[]; x=0
N=int(input())
if(N>=1 and N<=10**4):
    for i in range (N):
        t=int(input())
        if (-10**4<t<10**4):
            v= 3*t-4*(2*t*(3*(t-2)))
            
        if (v>0):
            L.append("Sentido: direita para esquerda")
        else:
            L.append("Sentido: esquerda para direita")
while x<(len(L)):
    print(L[x])
    x=x+1