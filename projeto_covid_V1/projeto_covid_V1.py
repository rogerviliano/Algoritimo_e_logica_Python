#cadastrar usuarios - nome,idade e sexo - OK
#cadastrar saudações - saudações dinamicas OK
#Cadastrar questionario_Diagnostico covid-4 perguntas relacionadas a sintomas
#Relatórios:
        #Consolidado Usuarios/sintomas
        #Consolidado Usuarios/faixa etária(adolescente,adulto e idoso)
        #Consolidado Usuario/Sexo
        #Consolidado Sexo Feminino com perda de paladar
        #Consolidado Adolescente com febre e tosse

#programa principal
from projeto_covid_V1_BACK import cadastro_usuario,relatorios
from projeto_covid_V1_FRONT import questionario,menu



list_entrevistados=[]
num_entre=0

nomes=[]
idades=[]
sexos=[]
faixas=[]
usuario_sintomas=[]
tupla_cidadao=(nomes,idades,sexos,faixas,usuario_sintomas)

lista_saudacoes =["Pesquisa - Teste Covid"]
list_cidadaos=[]
list_perguntas=[]

x=True
while x==True:
        menu(tupla_cidadao,list_perguntas,lista_saudacoes)
        cadastro_usuario(tupla_cidadao)
        questionario(tupla_cidadao,list_perguntas)
        relatorios(tupla_cidadao)








