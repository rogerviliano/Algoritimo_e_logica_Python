
from funcoes_gerais import saudacao
from funcoes_gerais import analise

#programa principal
saudacao()
print("Indique o numero de entrevistados:")
num_entr=int(input())
lista_resp=[]
dic_resp={}
n=1
febril=0 
tosse=0 
paladar=0
olfato=0
pal_olf=0

while n !=num_entr+1:
    print("Digite seu nome:")
    nome=input()
    print("---- Responda SIM ou NAO---")
    print("tem sintomas febris?")
    r21=(input()).lower()
    print("tem sintomas de tosse?")
    r22=(input()).lower()
    print("tem sintomas de falta de paladar?")
    r23=(input()).lower()
    print("tem sintomas falta de Olfato?")
    r24=(input()).lower()
    res=analise(r21,r22,r23,r24)
    if r21=="sim":
        febril+=1
    else:
        febril+=0
    if r22=="sim":
        tosse+=1
    else:
        tosse+=0
    if r23=="sim" and r24 =="sim":
        pal_olf+=1
        paladar+=1
        olfato+=1
    if r23=="nao" and r24=="sim":
        olfato+=1
        paladar+=0
        pal_olf+=1
    if r24=="não" and r23=="sim":
        paladar+=1
        olfato+=0
        pal_olf+=1


    lista_resp.append(nome) #adiciona nome a lista
    lista_resp.append(res) #adicionao situação a lista
    dic_resp[nome]=res #adiciona key e value ao dicionario
    n+=1 #atualiza contadora do while


print(febril,tosse,paladar,olfato,pal_olf)    
total={"febril":febril,"tosse":tosse,"Falta de paladar":paladar,"Perda de olfato":olfato,"F.Paladar/Olfato":pal_olf}
print(lista_resp) #imprime a lista atualizada com as respostas
print(dic_resp) #imprime odicionario com as avaliações
print(total) #imprima dicionario com os totais
    
    


