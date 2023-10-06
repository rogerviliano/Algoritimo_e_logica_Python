nomes=[]
cidadao=set()
estado=[]
cidade=[]
tup_cidadao=(nomes,estado,cidade)
x=True
while x==True:
    nome=input("Digite seu nome:\n")
    cpf=input("Digite seu CPF(xxx-xxx-xxx-xx):\n")
    estado=input("Digite seu Estado(URL)\n")
    cidade=input("Digite sua cidade Natal:\n")
    cad_cidadao=nome+"\n"+cpf+"\n"+cidade+"\n"+estado
    cidadao.add(cad_cidadao)
    sair=int(input("[1]Novo Cadastro [2]Sair"))
    if sair==2:
        x=False
    else:
        x=True

        
print("-----Relatório-----\n")

for i in cidadao:
    print(i)


#NAO ORDENOU CORRETAMENTE