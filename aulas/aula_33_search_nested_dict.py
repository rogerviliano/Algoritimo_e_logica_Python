brasil={}
i=0
j=0
print("Quantas regiões deseja cadastrar?:\n>> ")
qtd_reg=int(input())
print("Quantos estados?:\n>> ")
qtd_est=int(input())
while i < qtd_reg:
    print("Digite a Regiao:\n>>")
    reg=input()
    brasil[reg]={}
    while j < qtd_est:
        print("Digite o estado:\n>>")
        est=input()
        brasil[reg][est]={}
        print("Digite a capital:\n>>")
        cap=input()
        brasil[reg][est]=cap
        j+=1
    i+=1
    j=0

print("Escolha a Regiao para visualizar:")
regioes=brasil.keys()
for i in regioes:
    print(i)
regiao=input()
reg_print=brasil.get(regiao)
print(reg_print)
