#exs1
# arq=open("IMC.txt","w")
# C=1;h=0;m=0;PP=0;C1=[];C2=[];C3=[];M=[];d=0;S=[];i=0
# sets=str("CPF IDADE SEXO ALTURA  PESO")
# arq.write(str(sets)+"\n")
# while C<=2:
    # print("pessoa", C)
    # cpf=int(input("digite seu cpf \n"))
    # I=int(input("digite sua idade \n"))
    # s=int(input("digite seu sexo sendo 1= masculino 2= feminino \n"))
    # A=float(input("digite sua altura em metros (obs:use '.' ao invés de ',') \n"))
    # p=float(input("digite seu Peso \n"))
    # if cpf != 0 and I != 0 and s != 0 and A != 0 and p != 0:
        # arq.write(str(cpf)+"\t"+str(I)+"\t"+"\t"+str(s)+"\t"+str(A)+"\t"+"\t"+str(p)+"\n")
    # C=C+1
# arq.close()
# arq=open("IMC.txt","r")
# for linha in arq:
    # if i > 0:
        # L=linha[:-1].split('\t')
        # C1.append(float(L[4]))
        # C2.append(float(L[6]))
        # C3.append(int(L[3]))
    # else:
        # i=i+1
# arq.close()
# while PP<C-1:
    # if C3[PP] == 1:
        # h=h+1
    # elif C3[PP] == 2:
        # m=m+1
    # IMC=C2[PP]/((C1[PP])**2)
    # S.append(IMC)
    # y=len(C3)
    # PP=PP+1
# while d<C-1:
    # if S[d]<20:
        # M.append("Abaixo do peso")
    # elif S[d]>20 and S[d]<=25:
        # M.append("Peso Normal")
    # elif S[d]<25 and S[d]<=30:
        # M.append("Sobre Peso")
    # elif S[d]<30 and S[d]<=40:
        # M.append("Obeso")
    # elif S[d]<40:
        # M.append("Obeso Mórbido")
    # d=d+1
# print("Classificação de peso das pessoas em suas respectivas ordens:",M)
# print("total de homens:", h, "total de mulheres:", m, "total de pessoas", y)
################################################################
# Exs2
# C1=[];C2=[];C3=[];C4=[]
# arq=open("Atualizacao.txt")
# for linha in arq:
    # L=linha.split("\n")
    # C1.append(L)
# for i, frase in enumerate(C1):
    # C1[i] = frase[0].split()
    # for palavra in C1[i]:
        # p=palavra.split()
        # C2.append(p)
# L=len(C1)
# P=len(C2)
# arq.close()
# print("linhas arq 1:",L)
# print("Palavras arq 1:",P)
#############################
# arq=open("IONDATA.DAT")
# for linha in arq:
    # L=linha.split("\n" and "\x1a")
    # C3.append(L)
# for i, frase in enumerate(C3):
    # C3[i] = frase[0].split()
    # for palavra in C3[i]:
        # p=palavra.split()
        # C4.append(p)
# l=len(C3)
# p=len(C4)
# arq.close()
# print("linhas arq 2:",l)
# print("palavras arq 2:",p)
#############################################################################################
#EXS1 Otimizado
# arq=open("IMC.txt","w")
# C=1;h=0;m=0;M=[];i=0;SP=0;N=0;PP=0;O=0;OM=0
# sets=str("CPF IDADE SEXO ALTURA  PESO")
# arq.write(str(sets)+"\n")
# while C<=2:
    # print("pessoa", C)
    # cpf=int(input("digite seu cpf \n"))
    # I=int(input("digite sua idade \n"))
    # s=int(input("digite seu sexo sendo 1= masculino 2= feminino \n"))
    # A=float(input("digite sua altura em metros (obs:use '.' ao invés de ',') \n"))
    # p=float(input("digite seu Peso \n"))
    # if cpf != 0 and I != 0 and s != 0 and A != 0 and p != 0:
        # arq.write(str(cpf)+"\t"+str(I)+"\t"+"\t"+str(s)+"\t"+str(A)+"\t"+"\t"+str(p)+"\n")
    # C=C+1
# arq.close()
# arq=open("IMC.txt","r")
# for linha in arq:
    # if i > 0:
        # L=linha[:-1].split('\t')
        # IMC=(float(L[6]))/((float(L[4]))**2)
        # #print(IMC)
        # if IMC<20:
            # M.append("Abaixo do peso")
            # PP=PP+1
        # elif IMC>20 and IMC<=25:
            # M.append("Peso Normal")
            # N=N+1
        # elif IMC>25 and IMC<=30:
            # M.append("Sobre Peso")
            # SP=SP+1
        # elif IMC>30 and IMC<=40:
            # M.append("Obeso")
            # O=O+1
        # elif IMC>40:
            # M.append("Obeso Mórbido")
            # OM=OM+1
        # if L[3] == "1":
            # h=h+1
        # elif L[3] == "2":
            # m=m+1
    # else:
        # i=i+1
# arq.close()
# y=m+h
# print("Classificação de peso das pessoas em suas respectivas ordens:",M)
# print("Abaixo do Peso:",PP)
# print("Peso Normal:",N)
# print("Sobre Peso:",SP)
# print("Obeso:",O)
# print("Obeso Mórbido:",OM)
# print("total de homens:", h, "total de mulheres:", m, "total de pessoas", y)
###########################################################################################
