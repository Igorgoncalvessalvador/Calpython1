# Calculado s/ parametros

def Aula1s():

  n1 = int (input('Digite o primeiro número: '))
  n2 = int (input('Digite o segundo número: '))

  print('Soma:', n1,'+',n2,' = ',n1+n2)
  print('Subtração:', n1,'-',n2,' = ',n1-n2)
  print('Multiplicação:', n1,'*',n2,' = ',n1*n2)
  print('Divisão:', n1,'/',n2,' = ',n1/n2)
  print('Expoente:', n1,'**',n2,' = ',n1**n2)


#calculadora c/ parametros

def Aula1c(n1,n2,e):
  
  if e == '+':
    print('Somado=', n1+n2)
  elif e == '-':
    print('Subtraido=', n1-n2)
  elif e == '*':
    print('Multiplicado=', n1*n2)
  elif e == '/':
    print('Dividido=', n1/n2)
  elif e == '**':
    print('Expoente=', n1**n2)
  else:
    print('Verifique o operador')
