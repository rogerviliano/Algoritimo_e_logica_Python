import random
from projeto_covid_V1_BACK import diagnostico,relatorios,cad_cidadao,cad_perguntas,listar_cidadaos,listar_perguntas,cad_saudacoes,listar_saudacoes




def questionario(tupla_cidadao,list_perguntas):
    i=0
    for nome in tupla_cidadao[0]:
        print(">>",tupla_cidadao[0][i]," - Responda SIM ou NAO -")
        tupla_cidadao[4].append(nome)
        print("tem sintomas febris?")
        r21=(input()).lower()
        if r21 =="sim":
            tupla_cidadao[4].append("Febre")
        else:
            tupla_cidadao[4].append("x")
        print("tem sintomas de tosse?")
        r22=(input()).lower()
        if r22 =="sim":
            tupla_cidadao[4].append("Tosse")
        else:
            tupla_cidadao[4].append("x")
        print("tem sintomas de falta de paladar?")
        r23=(input()).lower()
        if r23 =="sim":
            tupla_cidadao[4].append("Falta de Paladar")
        else:
            tupla_cidadao[4].append("x")
        print("tem sintomas falta de Olfato?")
        r24=(input()).lower()
        if r24 =="sim":
            tupla_cidadao[4].append("Falta de Olfato")
        else:
            tupla_cidadao[4].append("x")
        i+=1
    return    

def menu(tupla_cidadao,list_perguntas,lista_saudacoes):
    print("BEM VINDO - ESCOLHA A OPÇÃO ABAIXO")
    menu=True
    while menu!=False:
        resp=int(input("[1]CADASTRAR [2]LISTAR [3]Relatórios [4]Iniciar Entrevista [5]Diagnostico [6]Sair "))
        if resp==1:
            resp2=int(input("[1]Cadastrar Cidadão [2]Cadastrar Perguntas Sintomas [3]Casdastrar Saudações"))
            if resp2==1:
                cad_cidadao(tupla_cidadao)
            if resp2==2:
                cad_perguntas(list_perguntas)
            if resp2==3:
                cad_saudacoes(lista_saudacoes)
        if resp==2:
            resp2=int(input("[1]Listar Cidadãos [2]Listar Perguntas Sintomas [3]Listar Saudações"))
            if resp2==1:
                listar_cidadaos(tupla_cidadao)
            if resp2==2:
                listar_perguntas(list_perguntas)
            if resp2==3:
                listar_saudacoes(lista_saudacoes)
        if resp==3:
            relatorios(tupla_cidadao)
        if resp==4:
            menu=False
        if resp==5:
            diagnostico(tupla_cidadao,list_perguntas)
        if resp==6:
            exit()
    return 