dict_alunos={"aluno":"João","Convidado":"Maria","Professor":"Paulo","Colega":"Abraão","Padre":"Lucas","Amigo":"Gilberto","Metrologista":"Roger"}
print("\n>>>>>>>>>Chaves:")
for x in dict_alunos:
    print(x) #recebe cada chave em x
    print(dict_alunos.values())#imprime uma lista com os valores

yy=dict_alunos.keys()
for i in yy:
    print("Chave: ",i)


print("\n>>>>>>>>>>Valores")
for y in dict_alunos: #y recebe 'key'
    xx=dict_alunos.get(y)#xx armazerna 'value' de y
    print(xx) #exibe valor de xx
print(len(dict_alunos))#comprimento do dicionario

dict_alunos.pop("Convidado")#remove elemento pela chave Convidado 
print(dict_alunos)

ff="Colega"
dict_alunos.pop(ff)
print(dict_alunos) #tambem pode ser passado por variavel