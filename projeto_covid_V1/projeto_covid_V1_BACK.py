


def cadastro_usuario(tupla_cidadao):
    numero_entrevistados=len(tupla_cidadao[0])
    n=0
    while n < numero_entrevistados:
        print(">> ",tupla_cidadao[0][n])
        idade=int(input("Digite sua idade: "))
        tupla_cidadao[1].append(idade)
        if idade<18:
            tupla_cidadao[3].append("Adolescente")
        if idade>18 and idade<=65:
            tupla_cidadao[3].append("Adulto")
        if idade>65:
            tupla_cidadao[3].append("Idoso")
        sexo=input("Digite seu sexo:[M] Masculino [F]Feminino : ").upper()
        tupla_cidadao[2].append(sexo)
        n+=1

    return 
    

def relatorios(tupla_cidadão):
    
    resp=0
    while resp!=6:
        print("Escolha o relatório desejado:\n[1]Usuarios/Sintomas\n[2]Usuarios/Faixa Etaria\n[3]Usuarios/Sexo\n[4]Feminino/perda de paladar\n[5]Adolescente/febre e tosse\n[6]Sair\n")
        resp=int(input())
        print("Tipo de relatório: [1]Analitico [2]Sintético:")
        resp2=int(input())
        if resp==1 and resp2==1:
            rel_usuario_sint(tupla_cidadão)
        if resp==2 and resp2==1:
            rel_usuario_faixa(tupla_cidadão)
        if resp==3 and resp2==1:
            rel_usuario_sexos(tupla_cidadão)
        if resp==4 and resp2==1:
            rel_fem_paladar(tupla_cidadão)
        if resp==1 and resp2==2:
            print("Relatório Sintético:\nNumero de Sintomaticos:",len(tupla_cidadão[0])) #ok
        if resp==2 and resp2==2:
            print("Relatório Sintético:\nFaixas Etárias:\nAdolescentes",tupla_cidadão[3].count("Adolescente"),"\nAdultos:",tupla_cidadão[3].count("Adulto"),"\nIdosos:",tupla_cidadão[3].count("Idoso"))
        if resp==3 and resp2==2:
            print("Relatório Sintético:\nNumero de Sintomaticos:",len(tupla_cidadão[0]))
        if resp==4 and resp2==2:
            print("Relatório Sintético:\nNumero de Sintomaticos:",len(tupla_cidadão[0]))
        
    return

    

 

def rel_usuario_faixa(tupla_cidadao):
    lista=len(tupla_cidadao[0])
    nome=0
    idade=0
    print("----Relatorio Usuario/Faixa Etaria----")
    while nome <= lista-1:
        print("Nome: ",tupla_cidadao[0][nome])
        print("Idade: ",tupla_cidadao[1][idade])
        if tupla_cidadao[1][idade] < 18:
            print("Faixa Etaria: Adolescente")
        if tupla_cidadao[1][idade] > 18 and tupla_cidadao[1][idade] < 60:
            print("Faixa Etaria: Adulto")
        if tupla_cidadao[1][idade] >= 60:
            print("Faixa Etaria: Idoso")
        print("-----------")
        idade+=1
        nome+=1
    return

        
def rel_usuario_sint(tupla_cidadão):
    user_=0
    sint1=1
    sint2=2
    sint3=3
    sint4=4
    lista=len(tupla_cidadão[4])
    print("----Relatorio Usuario/Sintomas----")
    while user_ < lista:
        print("---",tupla_cidadão[4][user_],"---")
        print(tupla_cidadão[4][sint1])
        sint1+=5
        print(tupla_cidadão[4][sint2])
        sint2+=5
        print(tupla_cidadão[4][sint3])
        sint3+=5
        print(tupla_cidadão[4][sint4])
        sint4+=5
        user_+=5

    return


def rel_usuario_sexos(tupla_cidadão):
    indice=0
    lis_fem=0
    list_masc=0
    print("----Relatorio Usuario/Sexos----")
    print("\nTotal de Usuarios: ",len(tupla_cidadão[0]),"\n_____")
    
    while indice < len(tupla_cidadão[0]):
        print("Usuario: ",tupla_cidadão[0][indice])
        if tupla_cidadão[2][indice]=="M":
            print("Sexo: Masculino\n_____")
            list_masc+=1
        else:
            print("Sexo: Feminino\n_____")
            lis_fem+=1
        indice+=1
    print("\nUsuarios Femininos: ",lis_fem)
    print("Usuarios Masculinos: ",list_masc)
    return

def rel_fem_paladar(tupla_cidadão):
    list_ind=[]
    list_nomes=[]
    ind_sex=0
    for ind in tupla_cidadão[2]:
        if ind =="F":
            list_ind.append(ind_sex)
            ind_sex+=1
        else:
            ind_sex+=1
    for nome in list_ind:
        list_nomes.append(tupla_cidadão[0][nome])
    i_nomes=0
    i_sint=3
    n=0
    list_nomes_pal=[]
    l=len(list_nomes)
    while n <= l-1:
        nome_pesq=list_nomes[n]
        sint_pesq="Falta de Paladar"
        nome_usu=usuario_sintomas[i_nomes]
        sint_usu=usuario_sintomas[i_sint]
        if nome_pesq==nome_usu and sint_pesq==sint_usu:
            list_nomes_pal.append(nome_usu)
            n+=1
            i_nomes+=5
            i_sint+=5
        else:
            n+=1
    print("-----Relatório FEM/PERDA DE PALADAR-----")
    n=1
    for user in list_nomes_pal:
        print(n,":",user)
        n+=1

    return


def cad_cidadao(tupla_cidadao):
    n_cidadao=int(input("Quantos cidadãos deseja cadastrar:\n"))
    x=1
    while x <= n_cidadao:
        print("Digite o nome do cidadão n°\n",x)
        nome=input()
        cpf=""
        while len(cpf)<11:
            print("Digite seu CPF:\n")
            cpf=input()
        cidadao=nome+"|"+cpf
        tupla_cidadao[0].append(cidadao)
        x+=1
    return

def cad_perguntas(list_perguntas):
    n_perguntas=int(input("Quantas perguntas deseja cadastrar:\n"))
    x=1
    while x <= n_perguntas:
        print("Digite pergunta n°",x)
        pergunta=input()
        list_perguntas.append(pergunta)
        x+=1
    return

def listar_cidadaos(tupla_cidadao):
    if tupla_cidadao[0]==[]:
        print("Lista Vazia - cadastre os cidadão no menu inicial")
    else:
        for i in tupla_cidadao[0]:
            print(i)
    return

def listar_perguntas(list_perguntas):
    if list_perguntas==[]:
        print("Lista Vazia - cadastre as perguntas no menu inicial")
    else:
        for i in list_perguntas:
            print(i)
    return


def cad_saudacoes(lista_saudacoes):
    resp=int(input("Quantas saudações deseja cadastrar?"))
    x=1
    while x <= resp:
        print("Digite a saudação n°",x)
        saudacao=input()
        lista_saudacoes.append(saudacao)
        x+=1
    return

def listar_saudacoes(lista_saudacoes):
    if lista_saudacoes==[]:
        print("Lista Vazia - cadastre as saudações no menu inicial")
    else:
        for i in lista_saudacoes:
            print(i)
    return


def diagnostico(tupla_cidadao,list_perguntas):
    print("Digite o CPF do Cidadão para saber o diagnostico:")  
    cpf=input()
    i=(-1)
    lista=tupla_cidadao[0]
    print(lista)
    i=0
    for cpf_ in lista:
        cpf_2=cpf_.split("|")
        if cpf_2[1]==cpf:
            print(tupla_cidadao[0][i])
        i+=1


    return

