torcedor={}
regiao={}
est_civis=[]

print("Digite o numero de torcedores: ")
n_torcedores=int(input())
x=0
while x < n_torcedores:
    nome=input("Nome:")
    idade=int(input("Idade:"))
    torcedor.update({nome:idade})
    estado=input("Estado:")
    cidade=input("Cidade:")
    regiao.update({estado:cidade})
    est_civil=input("Estado civil:")
    est_civis.append(est_civil)
    x+=1


lista=torcedor.keys()
print(lista)
print(torcedor.values())
print(regiao)
print(est_civis)
