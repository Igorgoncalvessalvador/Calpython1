#bibliotca para formatar data.
import numpy as np


import datetime

#
from collections import Counter

#
import collections

#
import pandas as pd

#
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


#Abrindo o arquivo e separando as posições.

ref_arquivo = open('GrupoBI.txt', "r", encoding='utf-8')
linha = ref_arquivo.readline()

list_datas = []
list_erros_formatacao = []
list_pessoas = []
list_msgs = []

while linha:
    linha = ref_arquivo.readline()
    try:
      date_time_obj = datetime.datetime.strptime(linha[1:17], '%d/%m/%y %H:%M:%S')
      list_datas.append(date_time_obj)
      msg = linha[20:]
      if(len(msg.split(':')) >= 2):
            list_pessoas.append(msg.split(':')[0])
            list_msgs.append(msg.split(':')[1])
    except ValueError:
      list_erros_formatacao.append('Falha na formatação')
ref_arquivo.close()


#Analise de quem mais manda mensagem no grupo.

dict_pessoas = dict(Counter(list_pessoas))
pessoas_df = pd.DataFrame(dict_pessoas.items(), columns=['Pessoa', 'Qnt Mensagem'])
pessoas_df = pessoas_df.sort_values(by=['Qnt Mensagem'], ascending=False)
pessoas_df['Pessoa'] = pessoas_df['Pessoa'].replace(['\u202a+55\xa011\xa095765‑5550\u202c','\u202a+55\xa081\xa09957‑6999\u202c','\u202a+55\xa011\xa098793‑6843\u202c','\u202a+55\xa011\xa097301‑7387\u202c','\u202a+55\xa013\xa099785‑0435\u202c','\u202a+55\xa011\xa095980‑8745\u202c','\u202a+55\xa011\xa099122‑8956\u202c'],['Oliveira','Rosane','Laisla','Mirella','Lopes','Alexandre','Jean'])
print(pessoas_df)
pessoas_df.plot(kind='barh', x = 'Pessoa', y = 'Qnt Mensagem', figsize=(20,10), color=['#fa9191', '#ff6969', '#a82525', '#6b0000', '#ed0000'])


#Exercicio 1 - Quais as palavras mais trocadas na conversa.

palavras = []
f = list_msgs
for i in f:
  i = i.split()
  for a in i:
    palavras.append(a)
    if len(a) < 2:
     palavras.remove(a)
dict_palavras = dict(Counter(palavras).most_common(6))
palavras_df = pd.DataFrame(dict_palavras.items(), columns=['Palavra', 'Quantidade'])
palavras_df = palavras_df.sort_values(by=['Quantidade'], ascending=False)
palavras_df.plot(kind='barh', x = 'Palavra', y = 'Quantidade', figsize=(13,7), color=['#fa9191', '#ff6969', '#a82525', '#6b0000', '#ed0000'])


#Exercicio 2 - Qual o dia da semana que mais troca mensagem.

dia_da_semana = {
  0: "domingo",
  1: "segunda",
  2: "terça",
  3: "quarta",
  4: "quinta",
  5: "sexta",
  6: "sabado"
}
list_horas = []
list_dia_semana = []
for data in list_datas:
    list_horas.append(data.time().hour)
    
    list_dia_semana.append(dia_da_semana.get(data.weekday()))
    
    if(data.weekday() == 1):
        list_dia_semana.append('segunda')
    elif(data.weekday() == 2):
        list_dia_semana.append('terça')
    elif(data.weekday() == 3):
        list_dia_semana.append('quarta')
    elif(data.weekday() == 4):
        list_dia_semana.append('quinta')
    elif(data.weekday() == 5):
        list_dia_semana.append('sexta')
    elif(data.weekday() == 6):
        list_dia_semana.append('sabado')
    elif(data.weekday() == 0):
        list_dia_semana.append('domingo')
      
dict_dia_semana = dict(Counter(list_dia_semana))

dict_dia_semana = dict(Counter(list_dia_semana))
dia_df = pd.DataFrame(dict_dia_semana.items(), columns=['Dias da semana', 'Frequencia'])
dia_df = dia_df.sort_values(by=['Frequencia'], ascending=False)
dia_df.plot(kind='barh', x = 'Dias da semana', y = 'Frequencia', figsize=(13,7), color=['#fa9191', '#ff6969', '#a82525', '#6b0000', '#ed0000'])

print('Quantidade de mensagens :')
dict_dia_semana

#Frequencia de mensagem em cada hórario.

sort_horas = sorted(dict_horas.items(), key=lambda x: x[1])
dict_horas = dict(Counter(list_horas))
horas_df = pd.DataFrame(dict_horas.items(), columns=['Horário', 'Frequencia'])
horas_df = horas_df.sort_values(by=['Frequencia'],ascending=False)
horas_df['Horário'] = horas_df['Horário'].astype('str')
horas_df['Horário'] = horas_df['Horário'].replace(['0','1','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'],['00h','01h','06h','07h','08h','09h','10h','11h','12h','13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h'])
horas_df.plot(kind='barh', x = 'Horário', y = 'Frequencia', figsize=(13,7), color=['#fa9191', '#ff6969', '#a82525', '#6b0000', '#ed0000'])

#Exercicio 3 - Qual o horario que mais fala. 
print('Qual o horario que menos fala:')
sort_horas[0]

#Exercicio 4 - Qual o horario que menos fala.
print('Qual o horario que mais fala:')
sort_horas[19]
