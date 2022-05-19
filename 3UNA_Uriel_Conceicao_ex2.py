###################Projeto###################
## Autor: Uriel Gonçalves Paiva da conceição
## Turma: FEAU-3UNA
## Matricula: 02010287
#############################################
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
L0=[];L1=[];L2=[];L3=[];L4=[];L5=[]
i=0;c=0;t=0;z=1
arq=open("Brazil.txt","r")
for linha in arq:
    if i > 1:
        L=linha[:-1].split('\t')
        Lt=linha
        data=datetime.strptime((L[0]),'%Y-%m-%d').date()
        L0.append(data)
        L1.append(float(L[2]))
        L2.append(float(L[4]))
        c=c+1
    else:
        i=i+1
arq.close()
while z<len(L2):
    L3.append(L1[z]-L1[t])
    L4.append(L2[z]-L2[t])
    L5.append((L0[t],L0[z]))
    t=t+1
    z=z+1
L5=np.array(L5, dtype='object')
L3=np.array(L3, dtype='object')
L4=np.array(L4, dtype='object')
plt.subplot(2,2,1)
plt.plot(L5,L3,'-b',label="novos_de_casos")
plt.title("diferença_dos_novos_de_casos")
plt.subplot(2,2,2)
plt.plot(L5,L4,'-r',label="novas_de_mortos")
plt.title("diferença_das_novas_de_mortos")
plt.show()
print(L5)