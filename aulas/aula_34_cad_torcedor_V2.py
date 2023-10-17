def cadastrar(dicionario):
    print("Quantos torcedores deseja cadastrar?\n")
    x=1
    n_torc=int(input())
    while x <= n_torc:
        print(">>> CPF:\n")
        cpf=int(input())
        dicionario[cpf]={}
        print(">>> Nome:\n")
        nome=input()
        dicionario[cpf]["Nome:"]=nome
        print(">>> Idade:\n")
        nome=input()
        dicionario[cpf]["Idade:"]=nome
        print(">>> Time:\n")
        nome=input()
        dicionario[cpf]["Time:"]=nome
        x+=1

def listar(dicionario):
    print(dicionario)
    return


def editar(dicionario):
    return  


cad_torcedor={}

x=99
while x==99:
    print("[1]Cadastrar [2]Listar [3]Editar [4]Sair")
    opcao=int(input())
    if opcao < 1 or opcao > 4:
        print("opção invalida")
    else:
        if opcao ==1:
            cadastrar(cad_torcedor)
        if opcao == 2:
            listar(cad_torcedor)
        if opcao == 3:
            editar(cad_torcedor)
        if opcao == 4:
            exit()

