estado=set() #declaração de uma estrutura tipo set vazio
x=True
while x==True:
    resp=input("Digite uma palavra para adicionar:[2]Sair")
    if resp=="2":
        x=False
    else:
        estado.add(resp)

print(estado)
for i in estado:
    if len(i)>4:
        print(i)
