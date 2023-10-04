import random
from frontEnd_functions import perguntas

def analise(r1,r2,r3,r4):
    if r3=="sim" and r4=="sim":
        r="Usuario deve ir urgente ao medico"
        return r
    else:
        if r1=="sim" and r2=="sim" and r3=="sim" and r4=="sim":
            r="Usuario deve ir urgente ao medico"
            return r
        if r3=="nao" and r4=="nao" and (r1=="nao" or r1=="sim" and r2=="nao" or r2=="sim"):
            r="Usuario deve aguardar em casa" 
            return r
        else:
            r="Usuario deve aguardar em casa" 
            return r

def contadora(febril,tosse,paladar,olfato,pal_olf,r21,r22,r23,r24):
    febril=febril 
    tosse=tosse
    paladar=paladar
    olfato=olfato
    pal_olf=pal_olf
    if r21=="sim":
        febril+=1
    else:
        febril+=0
    if r22=="sim":
        tosse+=1
    else:
        tosse+=0
    if r23=="sim" and r24 =="sim":
        pal_olf+=1
        paladar+=1
        olfato+=1
    if r23=="nao" and r24=="sim":
        olfato+=1
        paladar+=0
        pal_olf+=1
    if r24=="não" and r23=="sim":
        paladar+=1
        olfato+=0
        pal_olf+=1

    return febril,tosse,paladar,olfato,pal_olf


    

def respostas(num_users):
    tot_febril=0 
    tot_tosse=0 
    tot_paladar=0
    tot_olfato=0
    tot_pal_olf=0
    n=0
    list_resp=[]
    list_febril=[]
    list_all=[]
    entrevistados=[]
    while n !=num_users:
        nome,r21,r22,r23,r24=perguntas()
        entrevistados.append(nome)
        list_resp.append(nome)
        if r21=="sim":
            list_febril.append(nome)
        if r21=="sim" and r22=="sim" and r23=="sim" and r24=="sim":
            list_all.append(nome)   
        list_resp.append(analise(r21,r22,r23,r24))
        tot_febril,tot_tosse,tot_paladar,tot_olfato,tot_pal_olf=contadora(tot_febril,tot_tosse,tot_paladar,tot_olfato,tot_pal_olf,r21,r22,r23,r24)
        n+=1

    return list_resp, tot_febril,tot_tosse,tot_paladar,tot_olfato,tot_pal_olf,list_febril,entrevistados,list_all
        


    