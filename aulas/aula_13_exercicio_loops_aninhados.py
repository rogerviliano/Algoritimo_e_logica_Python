list_torcedores=[]
list_perg_perfil=[]
cont_inicial=True
while cont_inicial!=False:
    resp=int(input("--------- MENU --------\n[1]Cadastrar [2]listar\n"))
    if resp==1:
        resp2=int(input("[1]Cadastrar torcedores [2]Cadastrar Perguntas Perfil\n>>"))
        if resp2==1:
            cont_1=1
            n_torcedores=int(input("Quantos torcedores deseja cadastrar?\n>>"))
            while cont_1 <= n_torcedores:
                print("Digite o nome do torcedor ",cont_1)
                torcedor=input()
                list_torcedores.append(torcedor)
                cont_1+=1

        if resp2==2:
            cont_2=1
            n_perguntas=int(input("Quantas perguntas deseja cadastrar?\n>>"))
            while cont_2 <= n_perguntas:
                print("Digite a pergunta ",cont_2) 
                pergunta=input()
                list_perg_perfil.append(pergunta)   
                cont_2+=1
        
        if resp2!=1 and resp2!=2:
            print("Resposta Invalida.\nPrograma Encerrado")
            exit()
        cont_inicial=1
    if resp==2:
        resp_3=int(input("[1]Listar Torcedores Cadastrados [2]Listar Perguntas Perfil\n>>"))
        if resp_3==1:
            if list_torcedores==[]:
                print("Lista Vazia - Cadastre os torcedores no menu inicial")
            else:
                for i in list_torcedores:
                    print(i)
                print("Nº de cadastrados: ",len(list_torcedores))
        if resp_3==2:
            if list_perg_perfil==[]:
                print("Lista Vazia - Cadastre perguntas no menu inicial")
            else:
                for i in list_perg_perfil:
                    print(i)
                print("Nº de Perguntas: ",len(list_perg_perfil))
        if resp_3!=1 and resp_3!=2:
            print("Resposta Invalida.\nPrograma Encerrado")
            exit()            
    
        
    