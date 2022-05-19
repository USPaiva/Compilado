###################Projeto###################
## Autor: Uriel Gonçalves Paiva da conceição
## Turma: FEAU-3UNA
## Matricula: 01020287
#############################################
P= str (input("digite o Código do País \n")) ##insere o nome ou o codigo do país
PPT=float(input("digite a população total do País \n")) ## insere o total da população do país
D = 1 ##contagem dos dias
MM=0 ##total das mortes
while D<11: ##loop funciona para 10 dias
    print("Dia", D) ##mostra o dia q eh pra ser colocado
    M =float(input("digite o número de mortes do dia \n")) ##insere o numero de mortos em 10 dias no país
    MM = MM + M ##calculo da soma de mortes 
    D=D+1 ##  calculo de dias pro loop

MT= (MM/PPT)*100 ##conta de Mortes em 10 dias dividido pelo total da populção e convertido em %
print("total de mortes no", P, "foi", MT, "% da população")  ## Mostrar pro usuario a porcentagem de mortes da populção em relação a população total no perido de 10 dias apresentado