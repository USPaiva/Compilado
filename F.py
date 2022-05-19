###################Projeto#####################################
## Grupo Autor: Fênix
## Integrantes: Uriel Paiva, Felipe Franco, Paloma Machado
##############################################################
m=0;d=[];L=[];e=[];a=[];b=[];c=[];p=0;k=0
A=str(input())
B=str(input())
C=str(input())
D=str(input())
E=str(input())
x=str(input())
a.append(A)
b.append(B)
c.append(C)
d.append(D)
e.append(E)
while m<1:
    N=int(input())
    if N>=1 and N<=5*(10**3):
        m=m+1
while p<N:
    A=str(input())
    B=str(input())
    C=str(input())
    D=str(input())
    E=str(input())
    x=str(input())
    if A==a[0] and B==b[0] and C==c[0] and D==d[0] and E==e[0]:
        L.append("S")
    else:
        L.append("N")
    p=p+1
j=len(L)-1
while k<=j:
    f=j-k
    print(L[f])
    k=k+1