def cadastrar(dicionario):
    print("Quantos torcedores deseja cadastrar?\n")
    x=1
    n_torc=int(input())
    while x <= n_torc:
        print(">>> CPF:\n")
        cpf=int(input())
        dicionario[cpf]={}
        print(">>> Nome:\n")
        nome=input().upper()
        dicionario[cpf]["Nome:"]=nome
        print(">>> Idade:\n")
        nome=input()
        dicionario[cpf]["Idade:"]=nome
        print(">>> Sexo:\n")
        nome=input()
        dicionario[cpf]["Sexo:"]=nome
        x+=1

def relatorio(dicionario):
    sexo=[]
    adultos=[]
    adolescentes=[]
    homem=[]
    mulheres=[]
    for k in dicionario:
        dic=dicionario.get(k)
        for sk in dic:
            if sk=="Sexo:" and dic.get(sk)=="f":
                info=str(k)+"-"+dic.get("Nome:")
                sexo.append(info)
    print(sexo)


    print(dicionario)
    return


def editar(dicionario):
    return  


cad_torcedor={}

x=99
while x==99:
    print("[1]Cadastrar [2]Relatórios [3]Editar [4]Sair")
    opcao=int(input())
    if opcao < 1 or opcao > 4:
        print("opção invalida")
    else:
        if opcao ==1:
            cadastrar(cad_torcedor)
        if opcao == 2:
            relatorio(cad_torcedor)
        if opcao == 3:
            editar(cad_torcedor)
        if opcao == 4:
            exit()

