###################Projeto#####################################
## Grupo Autor: Fênix
## Integrantes: Uriel Paiva, Felipe Franco, Paloma Machado
##############################################################
C=0;d=0;L=[]
while C<1:
    N=int(input())
    if N>=1 and N<=10**3:
        C=C+1
while d<N:
    I=int(input())
    if I>=1 and I<=120:
        L.append(I)
        d=d+1
P=int(input())
m=sum(L)/N
NM=(sum(L)+P)/(N+1)
r=NM-m
if r>1:
    print("Media das idades aumenta em mais de 1 ano")
elif r<1 and r>0:
    print("Media das idades aumenta em menos de 1 ano")
elif r< -1:
    print("Media das idades diminui em mais de 1 ano")
elif r< 0 and r> -1:
    print("Media das idades diminui em menos de 1 ano")