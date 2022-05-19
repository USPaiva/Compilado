###################Projeto#####################################
## Grupo Autor: Fênix
## Integrantes: Uriel Paiva, Felipe Franco, Paloma Machado
##############################################################
C=0;d=0;L=[];x=0;t=0
while C<1:
    N=int(input())
    if N>=1 and N<=10**6:
        C=C+1
while d<1:
    K=int(input())
    if K>=1 and K<=10**6:
        d=d+1
while t<N:
    Ci=int(input())
    if Ci>=1 and Ci<=10**6:
        if Ci==K:
            x=1-(t/N)
        t=t+1
p=int(x*100)
print(p,'%')