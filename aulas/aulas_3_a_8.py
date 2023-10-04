#aulas 3 a 8 - intermediario

from backEnd_functions import respostas
from frontEnd_functions import saudacao,informar,menu

#programa principal
menu()
saudacao()
informar(*(respostas(int(input()))))
#*operador de descontrução dos parametros retornados pela função respostas








