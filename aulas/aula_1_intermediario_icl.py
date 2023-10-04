#AULA 1 - Escrevendo funções sem retorno

import random #importa a biblioteca de gerações randomicas

def saudacao():#nao retorna nada
    saud1 = "Bem vindo"
    saud2 = "Seja Bem vindo Usuario X"
    saud3 = "Ola, somos uma saudaçao aleatória"
    saud4 = "WELCOME USER"
    saud5 = "Hello My friend, welcome!"

    x=random.randint(1,4)#utilizando um função que retorna algo ], dentro de uma função que nao retorna nada
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
   
def menu():
    print("****MENU****")
    print("Digite [1]SIM ou [2]NÃO\n\n")

saudacao()#chamada da função de saudação
menu()#chamada da função menu

#função random - gerar numeros ramdomico a partir de um range/intervalo

n=random.randint(1,10)   
print(n)