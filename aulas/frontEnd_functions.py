import random

def menu():
    msg1="Opção Invalida"
    msg2="Programa Finalizado"
    msg3="TESTE COVID"
    resp=0
    print("*****MENU******")
    print("Digite [1]Responder [2]Sair")
    resp=int(input())
    if resp!=1 and resp!=2:
        menu()
    if resp==2:
        print(msg2)
        exit() 
    if resp==1:
        print(msg3)    

def saudacao():#nao retorna nada
    saud1 = "Ola! Vamos realizar o seu teste de Covid\nIndique o numero de entrevistados:"
    saud2 = "Seja Bem vindo ao teste Covid\nIndique o numero de entrevistados:"
    saud3 = "Pesquisa - Teste Covid\nIndique o numero de entrevistados:"
    saud4 = "Bem Vindo ao teste de Covid.\nIndique o numero de entrevistados:"
    saud5 = "Ola, responda as questoes do teste Covid\nIndique o numero de entrevistados:"
    x=random.randint(1,5)
    if x==1:
        print(saud1)
    if x==2:
        print(saud2)
    if x==3:
        print(saud3)
    if x==4:
        print(saud4)
    if x==5:
        print(saud5)

def informar(resposta,febril,tosse,paladar,olfato,pal_of,list_febril,entrevistados, list_all):
    print("total Febril: ",febril)
    print("total Tosse: ",tosse)
    print("total Paladar: ",paladar)
    print("total Olfato: ",olfato)
    print("total Paladar e Olfato: ",pal_of)
    print("Situação dos entrevistados: ",resposta) 
    print("Entrevistados: ",entrevistados)
    print("Entrevistados que apresentaram febre: ",list_febril)
    print("Apresentam todos os sintomas: ",list_all)    

def perguntas():
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

    return nome,r21,r22,r23,r24
