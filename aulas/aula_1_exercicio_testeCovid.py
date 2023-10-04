
from funcoes_gerais import saudacao
from funcoes_gerais import analise

#programa principal
saudacao()
print("Indique o numero de entrevistados:")
num_entr=int(input())
lista_resp=[]
dic_resp={}
n=1
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
    lista_resp.append(nome)#adiciona nome a lista
    lista_resp.append(res)#adicionao situação a lista
    dic_resp[nome]=res#adiciona
    n+=1
    
print(lista_resp) #imprime a lista atualizada com as respostas
print(dic_resp)
    
    


