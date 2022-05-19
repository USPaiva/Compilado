###################Projeto#####################################
## Grupo Autor: Fênix
## Integrantes: Uriel Paiva, Felipe Franco, Paloma Machado
##############################################################
Ci=5
Z=int(input())
if ((-10**6)<Z<(10**6)):
    R= Z*5
    if ((-10**6)<R<(10**6)):
        for i in range (5):
            R=Z*Ci
            Ci=Ci+1
            R2=R+Ci
            Ci=Ci-2
            R3=R2*(Ci)
            Ci=Ci+5
            R4=R3+(Ci)
            Ci=Ci-4
            R5=R4*(Ci)
print(R)
print(R2)
print(R3)
print(R4)
print(R5)
print(Z)


