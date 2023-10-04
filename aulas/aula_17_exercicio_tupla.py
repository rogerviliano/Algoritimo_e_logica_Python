list_nomes=["Nomes:"]
list_idades=["Idades:"]
list_sexos=["Sexos:"]
List_users=(list_nomes,list_idades,list_sexos)#inicia a tupla com sua estrutura-imutavel, porem com listas variaveis.
x=True
while x ==True:
    nome=input("Digite seu nome:\n")
    List_users[0].append(nome)
    idade=int(input("Digite sua idade:\n"))
    List_users[1].append(idade)
    sexo=int(input("Digite seu sexo:[1]Masc[2]Fem"))
    if sexo==1:
        List_users[2].append("Masculino")#ACESSA A TUPLA E ADICIONA NA LISTA DE INDICE 2(list_sexos)
    if sexo==2:
        List_users[2].append("Feminino")
    resp=int(input(">>>>>>>> Cadastrar novo[1]  Sair[2]\n"))
    if resp==1:
        x=True
    else:
        x=False
print("Nomes: ",List_users[0])
print("Idades: ",List_users[1])
print("Sexos : ",List_users[2])
print(List_users)
print(List_users[0][3])#ACESSA INDICE 3(QUARTO ITEM DA LISTA) DO INDICE 0(LISTA DE NOMES) DA TUPLA.

colunas=len(List_users)
linhas=len(list_nomes)
col=0
lin=0

while lin <linhas:
    while col<colunas:
        print(List_users[col][lin])
        col+=1
        lin+=1
    col=0
