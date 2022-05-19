########################################################################################
#n1=int(input("digite seu salario bruto\n"))
#n2=float(input("digite as horas extras\n"))
#n3=float(input("digite o valor horas extras\n"))
#sal_liq=(n1+(n2*n3))*0.92
#print("seu salario liquido é R$\n",sal_liq)
########################################################################################
# n1=float(input("digite uma nota\n"))
# n2=float(input("digite uma nota\n"))
# f=int(input("frequencia"))
# media=(n1+n2)/2
# if media>=5 and f>=18:
    # print("Aluno aprovado",media)
# elif media>=5 and f<18:
    # print("aluno reprovado por falta",media,f)
# elif f<18:
    # print("reprovado por falta")
# else:
    # print("reprovado",media)
########################################################################################
# n1=float(input("digite um numero\n"))

# if n1%3==0:
    # print("é multiplo de 3")
# else:
    # print("não é multiplo de 3")
#######################################################################################
# h=float(input("entre com sua altura em metros\n"))
# sexo=input("entre com seu sexo masculino ou feminino\n")
# if sexo=="masculino":
    # peso_ideal=(72.7*h)-58
    # print("o peso ideal é", peso_ideal)
# elif sexo=="femenino":
    # peso_ideal=(62.1*h)-44.7
    # print("o peso ideal é", peso_ideal)
# else:
    # print("sexo invalido")
    
#########################################################################################
# for f in range(1,51):
    # c=5*(f-32)/9
    # print(f,"em celsius",c)
##########################################################################################
# n=float(input("entre com um numero\n"))
# m=n%3
# print("o resto é", m)
##########################################################################################
# n=float(input("entre com a velocidade maxima da rodovia em km/h\n"))
# n2=float(input("entre com a velocidade do motorista em km/h\n"))
# if n2>n and n2<n+11:
    # print("motorista tem uma multa de R$50,00")
# elif n2>=n+11 and n2<n+31:
    # print("motorista tem uma multa de R$100,00")
# elif n2>=n+31:
    # print("motorista tem uma multa de R$200,00")
# else:
    # print("não há multa para pagar")
###########################################################################################
# n1=float(input("entre com um numero\n"))
# n2=float(input("entre com um numero\n"))
# n3=float(input("entre com um numero\n"))
# n4=float(input("entre com um numero\n"))

# if n1%2==0:
    # par1=n1
    # impar1=0
# else:
    # impar1=n1
    # par1=0
# if n2%2==0:
    # par2=n2
    # impar2=0
# else:
    # impar2=n2
    # par2=0
# if n3%2==0:
    # par3=n3
    # impar3=0
# else:
    # impar3=n3
    # par3=0
# if n4%2==0:
    # par4=n4
    # impar4=0
# else:
    # impar4=n4
    # par4=0
    
# p=par1+par2+par3+par4
# print("a soma dos numeros pares é", p)

# i=impar1+impar2+impar3+impar4
# print("a soma dos impares é",i)
################################################################################################
# n1=float(input("entre com o ano\n"))
# if n1%4==0 and n1%100!=0 or n1%400==0:
    # print("o ano", n1, "é bissexto")
# else:
    # print("o ano", n1, "não é bissexto")
 ################################################################################################
# x= 0
# for x in range(100):
    # print(x)
################################################################################################
# x=0
# for x in range(100):
    # if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 and x!=1 or x==2 or x==3 or x==5 or x==7:
        # print(x, "é primo")
#################################################################
# s1=float(input("Digite o salário do primeiro funcionário\n"))
# s2=float(input("Digite o salário do segundo funcionário\n"))
# s3=float(input("Digite o salário do terceiro funcionário\n"))
# i1=float(input("Digite a idade do primeiro funcionário\n"))
# i2=float(input("Digite a idade do segundo funcionário\n"))
# i3=float(input("Digite a idade do terceiro funcionário\n"))
# se1=float(input("Digite 1 se o primeiro funcionário for do sexo masculino ou 2 se feminino\n"))
# se2=float(input("Digite 1 se o segundo funcionário for do sexo masculino ou 2 se feminino\n"))
# se3=float(input("Digite 1 se o terceiro funcionário for do sexo masculino ou 2 se feminino\n"))
# if s1<1200 and i1<25 and se1==1:
    # A1=1     
    # B1=0     
# elif s1>5000 and i1>30 and se1==2:
    # A1=0     
    # B1=1     
# else:        
    # A1=0        
    # B1=0
# if s2<1200 and i2<25 and se2==1:
    # A2=1
    # B2=0
# elif s2>5000 and i2>30 and se2==2:
    # A2=0        
    # B2=1     
# else:        
    # A2=0        
    # B2=0
# if s3<1200 and i3<25 and se3==1:
    # A3=1
    # B3=0
# elif s3>5000 and i3>30 and se3==2:
    # A3=0 
    # B3=1
# else:
    # A3=0
    # B3=0
# m=A1+A2+A3
# n=B1+B2+B3
# print("numero de pessoas na condição A",m)
# print("numero de pessoas na condição B",n)

#####################################################################################

#EX6
# S= []
# T= []
# TI=float(input("Digite o tempo inicial \n"))
# TF=float(input("Digite o tempo Final \n"))
# P= (TF-TI)/100
# i = TI
# while i<TF:
    # T.append(i)
    # n = 0.75 *i**2 + 2.5 * i + 12
    # S.append(n)
    # i= i+P
# x = 0
# while x<100:
    # print("Tempo: ", T[x] ,", Espaço: ", S[x])
    # x= x+1

########################################################################################
#ex 9
# A= []
# i = 0
# t=0
# m=0
# while i<10:
    # V= int(input("digite valor \n"))
    # A.append(V)
    # i= i+1
# x=int(input("digite valor a ser buscado \n"))
# while t < len(A):
    # if A[t] == x:
        # m= m+1
  # t= t+1
# if m>=1:
    # print("achei")
# else:
    # print("não achei")

#########################################################################################
#ex 11
# A=[]
# B=[]
# i=0
# t=0
# while t==0:
    # n=float(input("digite a quantidade de elementos \n"))
    # if n<=10:
        # t=t+1
# while i<n:
    # V=float(input("digite um numero \n"))
    # if V>0 and V<=9:
        # A.append(V)
        # i=i+1
# X=float(input("digite o numero X \n"))
# B.append(X)
# c=B+A
# print(c)
#############################################################################################
# S= []
# T= []
# TI=0
# TF=100
# P= 2.5
# i = 0
# j = 0
# while i <= TF:
    # T.append(i)
    # n = i * 0.0393701
    # S.append(n)
    # i= i+P
    # j = j + 1 
# x = 0
# while x < j :
    # print("mm: ", T[x] ,", polegadas: ", S[x])
    # x= x+1
###########################################################################################
# N=float(input("Digite um numero \n"))
# m=0
# z=0
# X=[]
# somaX=0
# while somaX<N:
    # z=z+1
    # if z%2 != 0:
        # X.append(z)
        # somaX = sum(X)
        # m=m+1
# if m == N**0.5:
    # print(N,"é quadrado perfeito")
# else:
    # print(N,"não é quadrado perfeito")
##########################################################################################
# m=0
# x=0
# while m < 3:
    # N=float(input("Digite um numero \n"))
    # m=m+1
    # x= N+x
# z=x/m
# print("A média é",z)
##############################################################################################
# l = []
# T = []
# z=0
# t=0
# N=float(input("Digite um numero \n"))
# x=N
# while t<N:
    # while x>=1:
        # z=z+1
        # l.append(z)
        # x=x-1
        # m=l
    # print(m)
    # z=z+1
    # l.append(z)
    # del(l[0])
    # del(l[0])
    # T.append(1)
    # m=T+l
    # t=t+1
###############################################################################################
# x=float(input("Escreva o valor de x \n"))
# z=float(input("Escreva o valor de z \n"))
# xinicial=x

# while z<=x:
    # z=float(input("Escreva um novo valor para z, maior que x \n"))

# l=[]
# c=x
# while x<=z:
    # x=x+c
    # l.append(c)
    # c=c+1
# if sum(l)<z:
       # l.append(c)
# print("valores de x e z: x=", xinicial, "z=", z)
# print("numero de elementos na lista:", len(l))
# print("lista:",l, "soma dos valores", sum(l))
################################################################################################
# n= "Uriel"
# z=0
# x=len(n)
# l=0
# m=0
# while m<len(n):
    # print("*"*(x-1),n[l],"*"*(z))
    # x=x-1
    # l=l+1
    # z=z+1
    # m=m+1
#############################################################################################
# l = []
# z=0
# t=0
# N=float(input("Digite um numero \n"))
# x=N
# while t<N:
    # while x>=1:
        # z=z+1
        # l.append(z)
        # x=x-1
    # print(l)
    # del(l[0])
    # z=z+1
    # l.append(z)
    # t=t+1
##############################################################
# l = []
# T = []
# matriz=[]
# z=0
# t=0
# N=float(input("Digite um numero \n"))
# x=N
# while t<N:
    # while x>=1:
        # z=z+1
        # l.append(z)
        # x=x-1
        # m=l
    # m=T+l
    # z=z+1
    # matriz.append(m)
    # l.append(z)
    # del(l[0])
    # if len(l)>=1 and N != 1:
        # del(l[0])
    # if len(l)>N-2:
        # del(l[0])
        # T.append(1)
    # T.append(1)
    # t=t+1
# for lista in matriz:
    # for elemento in lista:
        # print(elemento, end=' ')
    # print()
################################################################
# N=float(input("Digite um numero de frangos \n"))
# x= N*4 #identificação
# z= (N*2)*3.5 ##alimento
# t=z+x
# print("a granja ira gastar",t,"no total")
#################################################################
# LS=[]
# LI=[]
# LSE=[]
# c=1
# t=0
# m=0
# h=0
# while c<=5:
    # print("funcionario",c)
    # S=float(input("Digite seu salario \n"))
    # LS.append(S)
    # I=float(input("Digite sua idade \n"))
    # LI.append(I)
    # SE=float(input("Digite seu genero sendo 1 Homem e 2 Mulher \n"))
    # LSE.append(SE)
    # c=c+1
# while t<5:
    # if LS[t]<1200 and LI[t]<25 and LSE[t]==2:
        # m=m+1
    # elif LS[t]>5000 and LI[t]>30 and LSE[t]==1:
        # h=h+1
    # t=t+1
# print("funcionarios homens que atendem o requisito", h)
# print("funcionarias mulheres que atendem o requisito", m)
##########################################################################
# i=0
# d=0
# while i<10:
    # n=float(input("digite um valor \n"))
    # if n % 2 == 0 and n!=0:
        # d=d+1
    # i=i+1
# print("a quantidade de numeros pares é",d)
#########################################################################
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Matriz impressa de outra forma:")
# for lista in matriz:
    # for elemento in lista:
        # print(elemento, end=' ')
    # print()
#########################################################################
# l = []
# T = []
# matriz = []
# z=0
# t=0
# N=float(input("Digite um numero \n"))
# x=N
# while t<N:
    # while x>=1:
        # z=z+1
        # l.append(z)
        # x=x-1
    # m=T+l
    # matriz.append(m)
    # z=z+1
    # l.append(z)
    # del(l[0])
    # del(l[0])
    # T.append(1)
    # t=t+1
# for lista in matriz:
    # for elemento in lista:
        # print(elemento, end=' ')
    # print()
#############################################################
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
# import numpy as np
# M=np.zeros((3,3))
# for i in range(M.shape[0]):
    # for j in range(M.shape[1]):
        # M[i,j]=i+j
# print(M)
##################################################################################
# L1=[];C=[];C1=[]
# i=0;c=0;x=1;s=3
# arq=open("2016I01Fa.txt","r")
# for linha in arq:
    # if i > 2:
        # L=linha[:-1].split('\t')
        # L2=linha
        # LN=int(L[2])-int(L[4])
        # L1.append(LN)
        # C.append(str(L2))
        # c=c+1
    # else:
        # L3=linha
        # C.append(str(L3))
        # i=i+1
# arq.close()
# for linha in C:
    # L=linha.split('\n')
    # C1.append(L)
# arq=open("diferença de colunas.txt","w")
# arq.write(str("resultados da diferença")+"\n"+str(C1[0][0])+"\n"+str(C1[1][0])+"\n"+str(C1[2][0])+"\t"+str("phF2-h'p")+"\n")
# while x<c:
    # arq.write(str(C1[s][0])+"\t"+str(L1[x])+"\n")
    # x=x+1
    # s=s+1
# arq.close()
###################################################################################################################################
# C=0
# while C<1:
    # N=int(input("Entre com a quantidade de testes \n"))
    # if N>=1 and N<=2000:
        # C=C+1

# l1=[]
# c=0

# while c<N:
    # A=int(input("Entre com o valor A \n"))
    # B=int(input("Entre com o valor B \n"))
    # K=int(input("Entre com o valor K \n"))
    # Z=int(input("Entre com o valor Z \n"))
    # x=((180-K+Z)/(A+B))
    # a=(A*x)+K
    # b=(B*x)-Z
    # if a+b==180:
        # l1.append("S")
    # else:
        # l1.append("N")
    # c=c+1

# print(l1)

# C=0;P=0;m=0;L=[]
# while C<1:
    # N=int(input())
    # if N>=1 and N<=2000:
        # C=C+1
# while P<N:
    # A=int(input())
    # B=int(input())
    # K=int(input())
    # Z=int(input())
    # x=((180-K+Z)/(A+B))
    # a=(A*x)+K
    # b=(B*x)-Z
    # if a+b==180:
        # L.append("S")
    # else:
        # L.append("N")
    # P=P+1
# print(L)
# while len(L)>m:
    # print(L[m])
    # m=m+1
#######################################################################    
# C=[];C00=[];C0=[];C1=[];C2=[];C3=[];C4=[];C5=[];c=0;x=1;t=0;n=1;i=0;s=0
# arq=open("2016I01Fa.txt","r")
# for linha in arq:
    # if i > 2:
        # L=linha[:-1].split('\t')
        # C00.append(str(L[0]))
        # C0.append(str(L[1]))
        # C1.append(int(L[2]))
        # C2.append(float(L[3].replace(",",".")))
        # C3.append(int(L[4]))
        # C4.append(str(L[5]))
        # C5.append(str(L[6]))
        # c=c+1
    # else:
        # L2=linha 
        # C.append(str(L2))
        # i=i+1
# arq.close()
# arq=open("resultados.txt","w")
# arq.write(str("resultados da diferença")+"\n"+str(C[s])+str(C[s+1])+str("UT")+"\t"+str("LT")+"\t"+str("h'F")+"\t"+str("foF2")+"\t"+str("phF2")+"\t"+str("SF")+"\t"+str("ES")+"\n")
# while x<c:
    # hF=C1[n]-C1[t]
    # foF2=C2[n]-C2[t]
    # phF2=C3[n]-C3[t]
    # arq.write(str(C00[t])+"\t"+str(C0[t])+"\t"+str(hF)+"\t"+str(foF2)+"\t"+str(phF2)+"\t"+str(C4[t])+"\t"+str(C5[t])+"\n")
    # t=t+1
    # n=n+1
    # x=x+1
# arq.close()
# print(C)
#######################################################
# d=0;x=0;l=[]
# while d<1:
    # N=int(input("Entre com o número de testes entre 1 e 2000 \n"))
    # if (1<=N<=2000):
        # d=d+1

# for c in range(0,N):
    # V=int(input("Entre com o número do painel de leds \n"))
    # if (1<=V<=10**5):  
        # F=list(str(V))
        # n=0
        # for i in F:
            # if i=="0":
                # n=n+6
            # if i=="1":
                # n=n+2
            # if i=="2":
                # n=n+5
            # if i=="3":
                # n=n+5
            # if i=="4":
                # n=n+4
            # if i=="5":
                # n=n+5
            # if i=="6":
                # n=n+6
            # if i=="7":
                # n=n+3
            # if i=="8":
                # n=n+7
            # if i=="9":
                # n=n+6
        # l.append(n)
    # else:
        # print("Este número não é válido")

# while x<N:
    # print(l[x])
    # x=x+1
##########################################################################################################
# L1=[];C=[];C1=[]
# i=0;c=0;x=1;s=3
# arq=open("2016I01Fa.txt","r")
# for linha in arq:
    # if i > 2:
        # L=linha[:-1].split('\t')
        # L2=linha
        # LN=int(L[2])-int(L[4])
        # L1.append(LN)
        # C.append(str(L2))
        # c=c+1
    # else:
        # L3=linha
        # C.append(str(L3))
        # i=i+1
# arq.close()
# for linha in C:
    # L=linha.split('\n')
    # C1.append(L)
# arq=open("diferença de colunas.txt","w")
# arq.write(str("resultados da diferença")+"\n"+str(C1[0][0])+"\n"+str(C1[1][0])+"\n"+str(C1[2][0])+"\t"+str("phF2-h'p")+"\n")
# while x<c:
    # arq.write(str(C1[s][0])+"\t"+str(L1[x])+"\n")
    # x=x+1
    # s=s+1
# arq.close()
# ##########################################################################################################
# d=0;x=0;l=[];p=[];z=0;c=0;t=0
# while d<1:
    # N=int(input("Entre com o número de testes entre 1 e 2000 \n"))
    # if (1<=N<=2000):
        # d=d+1
# while c<N:
    # V=int(input("Entre com o número do painel de leds \n"))
    # if (1<=V<=10**7):  
        # p.append(str(V))
        # n=0
        # while z<len(p[0]):
            # i=p[0][z]
            # if i=="0":
                # n=n+6
            # if i=="1":
                # n=n+2
            # if i=="2":
                # n=n+5
            # if i=="3":
                # n=n+5
            # if i=="4":
                # n=n+4
            # if i=="5":
                # n=n+5
            # if i=="6":
                # n=n+6
            # if i=="7":
                # n=n+3
            # if i=="8":
                # n=n+7
            # if i=="9":
                # n=n+6
            # z=z+1
        # z=0
        # l.append(n)
        # del(p[0])
    # else:
        # print("Este número não é válido")
    # c=c+1

# while x<N:
    # print(l[x])
    # x=x+1
########################################################################################################
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
# L0=[];C=[];L1=[];L2=[];L3=[];L4=[]
# i=0;c=0;x=1;s=3
# arq=open("Brazil.txt","r")
# for linha in arq:
    # if i > 0:
        # L=linha[:-1].split('\t')
        # Lt=linha
        # data=datetime.strptime((L[0]),'%Y-%m-%d').date()
        # L0.append(data)
        # L1.append(float(L[1]))
        # L2.append(float(L[2]))
        # L3.append(float(L[3]))
        # L4.append(float(L[4]))
        # c=c+1
    # else:
        # Lx=linha
        # C.append(str(Lx))
        # i=i+1
# arq.close()
# L0=np.array(L0, dtype='object')
# L1=np.array(L1, dtype='object')
# L2=np.array(L2, dtype='object')
# L3=np.array(L3, dtype='object')
# L4=np.array(L4, dtype='object')
# plt.subplot(2,2,1)
# plt.plot(L0,L1,'-r',label="total_de_casos")
# plt.title("total_de_casos")
# plt.subplot(2,2,2)
# plt.plot(L0,L2,'-b',label="novos_casos")
# plt.title("novos_casos")
# plt.subplot(2,2,3)
# plt.plot(L0,L3,'-g',label="total_de_mortos")
# plt.title("total_de_mortos")
# plt.subplot(2,2,4)
# plt.plot(L0,L4,'-y',label="novos_mortos")
# plt.title("novos_mortos")
# plt.tight_layout()
# plt.show()
#########################################################################
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
# L0=[];C=[];L1=[];L2=[];L3=[];L4=[];L5=[]
# i=0;c=0;x=1;s=3
# arq=open("Brazil.txt","r")
# for linha in arq:
    # if i > 0:
        # L=linha[:-1].split('\t')
        # Lt=linha
        # data=datetime.strptime((L[0]),'%Y-%m-%d').date()
        # L0.append(data)
        # L1.append(float(L[1]))
        # L2.append(float(L[2]))
        # L3.append(float(L[3]))
        # L4.append(float(L[4]))
        # c=c+1
    # else:
        # Lx=linha
        # C.append(str(Lx))
        # i=i+1
# arq.close()
# print("menor data é",min(L0))
# print("maior data é",max(L0))
# data1=input("digite a data inicial, no formato Y-m-d\n")
# data2=input("digite a data final, no formato Y-m-d\n")
# data1=datetime.strptime(data1,'%Y-%m-%d').date()
# data2=datetime.strptime(data2,'%Y-%m-%d').date()
# L00=[]
# for i in range(L0.shape[0]):
    # if L0[i]>=data1 and L0[i]<=data2:
        # T=[]
        # T.append(i)
        # L00.append(L0[i])
# L00=np.array(L00, dtype='object')
# L1=np.array(L1, dtype='object')
# L2=np.array(L2, dtype='object')
# L3=np.array(L3, dtype='object')
# L4=np.array(L4, dtype='object')
# plt.subplot(2,2,1)
# plt.plot(L00,L1,'-r',label="total_de_casos")
# plt.title("total_de_casos")
# plt.subplot(2,2,2)
# plt.plot(L00,L2,'-b',label="novos_casos")
# plt.title("novos_casos")
# plt.subplot(2,2,3)
# plt.plot(L00,L3,'-g',label="total_de_mortos")
# plt.title("total_de_mortos")
# plt.subplot(2,2,4)
# plt.plot(L00,L4,'-y',label="novos_mortos")
# plt.title("novos_mortos")
# plt.tight_layout();plt.show()
##############################################################
# exs 2
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
# L0=[];L1=[];L2=[];L3=[];L4=[];L5=[]
# i=0;c=0;t=0;z=1
# arq=open("Brazil.txt","r")
# for linha in arq:
    # if i > 0:
        # L=linha[:-1].split('\t')
        # Lt=linha
        # data=datetime.strptime((L[0]),'%Y-%m-%d').date()
        # L0.append(data)
        # L1.append(float(L[2]))
        # L2.append(float(L[4]))
        # c=c+1
    # else:
        # i=i+1
# arq.close()
# while z<len(L2):
    # L3.append(L1[z]-L1[t])
    # L4.append(L2[z]-L2[t])
    # L5.append((L0[z],L0[t]))
    # t=t+1
    # z=z+1
# L5=np.array(L5, dtype='object')
# L3=np.array(L3, dtype='object')
# L4=np.array(L4, dtype='object')
# plt.subplot(2,2,1)
# plt.plot(L5,L3,'-b',label="novos_de_casos")
# plt.title("diferença_dos_novos_de_casos")
# plt.subplot(2,2,2)
# plt.plot(L5,L4,'-r',label="novas_de_mortos")
# plt.title("diferença_das_novas_de_mortos")
# plt.show()
###############################################################################################
# EXs 1
# import numpy as np
# import matplotlib.pyplot as plt
# from datetime import datetime
# L0=[];L1=[];L2=[];L3=[];L4=[];L5=[]
# i=0;c=0;t=0;z=1
# arq=open("Brazil.txt","r")
# for linha in arq:
    # if i > 0:
        # L=linha[:-1].split('\t')
        # Lt=linha
        # data=datetime.strptime((L[0]),'%Y-%m-%d').date()
        # L0.append(data)
        # L1.append(float(L[1]))
        # L2.append(float(L[3]))
        # c=c+1
    # else:
        # i=i+1
# arq.close()
# L0=np.array(L0, dtype='object')
# L1=np.array(L1, dtype='object')
# L2=np.array(L2, dtype='object')
# plt.subplot(2,2,1)
# plt.plot(L0,L1,'-b',label="total_de_casos")
# plt.title("total_de_casos")
# plt.subplot(2,2,2)
# plt.plot(L0,L1,'-r',label="total_de_mortos")
# plt.title("total_de_mortos")
# plt.show()
#################################################################################################
# import requests; import numpy as np; import matplotlib.pyplot as plt; from datetime import datetime
# LTOTAL=[];L0=[]
# i=0;t=0;g=1
# def Baixar_arquivo(url, endereco):
    # resposta= requests.get(url)
    # if resposta.status_code == requests.codes.OK:
        # with open(endereco, 'wb') as novo_arq:
            # novo_arq.write(resposta.content)
        # print("Download Completo. Salvo como: {}".format(endereco))
    # else:
        # resposta.raise_for_status()
# if __name__ == "__main__":
    # Baixar_arquivo('https://covid.ourworldindata.org/data/owid-covid-data.csv','owid-covid-data.csv')
# arq=open("owid-covid-data.csv","r")
# for linha in arq:
    # L=linha[:-1].split(',')
    # Lt=linha
    # if i > 0:
        # data=datetime.strptime((L[3]),'%Y-%m-%d').date()
        # L0.append(data)
        # LTOTAL.append(L)
    # else:
        # LTOTAL.append(L)
        # i=i+1
# arq.close()
# while t<1:
    # RLT=[];RLTF=[];LD=[];LM=[];LP=[];MD=[];LR=[];N=[];LMF=[];LPF=[];LRF=[];MDS=[];NS=[]
    # c=0;z=0;x=0;v=0;n=0;f=0;k=0;h=0
    
    # cod=input("digite o iso code do país que deseja, sendo BRA:Brasil, ARG:Argentina, PRY:Paraguai, USA:Estados Unidos e CAN:Canada, ou qualquer outro iso code valido:\n")
    # p=int(input("1 para colocar grade no grafico e 0 para tirar a grade:\n"))
    # a=int(input("1 para colocar legenda no grafico e 0 para tirar a legenda:\n"))
    # print("Data limite Minima:",min(L0),"\nData limite Maxima:",max(L0))
    # data1=input("digite a data inicial, no formato Y-m-d\n")
    # data2=input("digite a data final, no formato Y-m-d\n")
    # data1=datetime.strptime(data1,'%Y-%m-%d').date()
    # data2=datetime.strptime(data2,'%Y-%m-%d').date()
    # if p==1:
        # q=True
    # else:
        # q=False
    # while h<1:
        # if data1<min(L0) or data2>max(L0):
            # data1=input("digite a data inicial novamente, no formato Y-m-d\n")
            # data2=input("digite a data final novamente, no formato Y-m-d\n")
            # data1=datetime.strptime(data1,'%Y-%m-%d').date()
            # data2=datetime.strptime(data2,'%Y-%m-%d').date()
        # else:
            # h=h+1
    # while c<len(LTOTAL):
        # if LTOTAL[c][0]==cod:
            # RLT.append(LTOTAL[c])
        # c=c+1
    # while z<len(RLT):
        # j=datetime.strptime((RLT[z][3]),'%Y-%m-%d').date()
        # if data1<=j<=data2:
            # RLTF.append(RLT[z])
        # z=z+1
    # while x<len(RLTF):
        # LD.append(RLTF[x][3])
        # if RLTF[x][7]=='':
            # LM.append(str(RLTF[x][7]).replace('','0'))
        # else:
            # LM.append(str(RLTF[x][7]))
        # if RLTF[x][44]=='':
            # LP.append(str(RLTF[x][44]).replace('','0'))
        # else:
            # LP.append(str(RLTF[x][44]))
        # if RLTF[x][16]=='':
            # LR.append(str(RLTF[x][16]).replace('','0'))
        # else:
            # LR.append(str(RLTF[x][16]))
        # x=x+1
    # while k<len(LP):
        # LMF.append(float(LM[k]))
        # LPF.append(float(LP[k]))
        # LRF.append(float(LR[k]))
        # k=k+1
    # while v<len(LP):
        # MT=(LMF[v]/LPF[v])*100
        # MD.append(MT)
        # MDS.append(str(MT))
        # v=v+1
    # while n<len(MD):
        # MM=(LRF[n]/MD[n])
        # N.append(MM)
        # NS.append(str(MM))
        # n=n+1
    # arq=open("3UNA_Uriel_Goncalves_ex1_{}.txt".format(g),"w")
    # arq.write(str("Autor: Uriel Gonçalves Paiva da conceição\nTurma: FEAU-3UNA\nMatricula: 02010287\n"))
    # arq.write(str("iso_code\tData\tTotal_de_Mortos\tPopulação\tTaxa_de_Reprodução\t%_de_Mortes_diarias_em_relação_a_população\tTaxa_de_reprodução_diario_em_relação_a_população_diaraia\n"))
    # while f<len(LP):
        # arq.write(str(cod+"\t"+LD[f]+"\t"+LM[f]+"\t"+LP[f]+"\t"+LR[f]+"\t"+MDS[f]+"\t"+NS[f]+"\n"))
        # f=f+1
    # arq.close()   
    # w=60
    # LD=np.array(LD, dtype='object')
    # LMF=np.array(LMF, dtype='object')
    # MD=np.array(MD, dtype='object')
    # N=np.array(N, dtype='object')
    # plt.figure(figsize=(16, 8))
    # plt.subplot(2,2,1)
    # plt.plot(LD,MD,'-b',label="relação_diaria_%_Mortos_/_População")
    # plt.xticks(rotation=w);plt.title("relação diaria do total de mortos com o total da população do país")
    # plt.xlabel("(Data)")
    # plt.ylabel("(%_de_(mortos/população))")
    # if a==1:
        # plt.legend(fontsize=10)
    # plt.grid(q)
    # plt.subplot(2,2,2)
    # plt.plot(LD,LM,'-r',label="total_de_mortos")
    # plt.xticks(rotation=w);plt.title("total de mortos do País")
    # plt.xlabel("(Data)")
    # plt.ylabel("(Total de mortos)")
    # if a==1:
        # plt.legend(fontsize=10)
    # plt.grid(q)
    # plt.subplot(2,2,3)
    # plt.plot(LD,N,'-g',label="relação_%_de_natalidade_/_%_de_mortalidade")
    # plt.xticks(rotation=w);plt.title("taxa de reprodução diario em relação ao total de mortes País")
    # plt.xlabel("(Data)")
    # plt.ylabel("(%de reprodução/%de mortes)")
    # if a==1:
        # plt.legend(fontsize=10)
    # plt.grid(q)
    # plt.tight_layout()
    # plt.savefig('3UNA_Uriel_Goncalves_ex1_{}.png'.format(g))
    # plt.show()
    # t=int(input("digite 0 para fazer outra analise ou 1 para parar\n"))
    # g=g+1
    #################################################
# for linha in arq:
    # c=linha[:-1].split(',')
    # data=datetime.strptime(c[3],'%Y-%m-%d').date()
    # if c[4]=='':
        # k=0
    # else:
        # k=c[4]
    # if c[5]=='':
        # k2=0
    # else:
        # k2=c[5]
    # if c[6]=='':
        # k3=0
    # else:
        # k3=c[6]
    # Dados.append([c[0],c[1],c[2],data,float(k),float(k2),float(k3)])
# arq.close()
##################################################################################
# import numpy as np
# from numpy import linalg
# import time
# import timeit
# E = np.array([[9,-5,-2,-3],
              # [-3,4,2,-7],
              # [-6,0,4,8]], dtype='double')
# if len(E[:,0]) == 3 and len(E[0,:])==4:
  # print(E)
# print("............................................")
# A = np.delete(E, 3, axis=1)
# print(A)
# print("............................................")
# print(abs(A[0,1]))
# print("............................................")
# print(abs(A[0,1])+ abs(A[0,2]))
# beta1 = (abs(A[0,1])+ abs(A[0,2]))/abs(E[0,0])
# print("............................................")
# print(beta1)
# print("............................................")
# print((abs(A[0,1])+ abs(A[0,2]))/abs(A[0,0]))
# beta2 = (beta1*abs(E[1,0])+ abs(A[1,2]))/abs(E[1,1])
# beta3 = (beta1*abs(E[2,0])+ beta2*abs(E[2,1]))/abs(E[2,2])
# beta = max([beta1, beta2, beta3])
# if beta > 1:
  # print('Não satisfaz o critério de convergência de Sasssenfeld porque beta = {} > 1'.format(beta))
# else:
  # print('Satisfaz 0 critério de convergência de Sasssenfeld porque beta = {} < 1'.format(beta))
#################################
# Xi=(float(input("Xi: ")))
# n=(float(input("n: ")))
# Sn=Xi*n
# print(Sn)
# t=0
# c=0
# Xi=3.57
# n=16000
# while c<n:
    # t=t+Xi
    # c=c+1
# Sn=t
#print(float(Sn))
#############################################################
C=0
N=(int(input("valor de N")))
R=(int(input("valor de R")))
while c ==0:
    if 1 <= N <= 5000:
        if 1 <= R <= 10**9:
            
            c=c+1