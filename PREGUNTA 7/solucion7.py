import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
url = 'https://raw.githubusercontent.com/OsvaldoRodriguez/PRIMER-PARCIAL-INF-354/master/DATASET/codechef2.csv'
datos = pd.read_csv(url, encoding="unicode_escape", on_bad_lines='skip');
dataset = datos.to_numpy()
titles = ['Global Rank', 'Stars', 'Username', 'Country', 'Country Rank', 'Rating', 'Highest Rating', 'Fully Solved', 'Partially Solved', 'Last Contest', 'Institute', 'Cycles o indices']

def mostrar(arr):
  print()
  for i in arr:
    print(i)
  print()
# print(dataset)
# print("DATASET ORIGINAL")
# print(datos)
# print(datos.columns)


for _ in range(2):
  print("CICLO NUMERO" , _)
  nuevoDato = []
  tam_muestra = 9272
  # tam_muestra = 100;
  for i in range(tam_muestra):
    nuevo = []
    for j in range(len(dataset[i])):
      nuevo.append(dataset[i][j])
    nuevo.append(i)
    nuevoDato.append(nuevo)

  # volviendolo aleatorio
  random.shuffle(nuevoDato)

  print('despues del shuffle')
  mostrar(nuevoDato)

  train = int(tam_muestra * 0.8)
  array_train = nuevoDato[:train]
  array_test = nuevoDato[train:]

  print("tamaño del train", len(array_train))
  print("tamaño del test", len(array_test))
  # mostrar(array_train)
  # print("test")
  # mostrar(array_test)

  # generando por columnas cualquier columna

  print("\ngenerando por columan el train")
  # print(len(nuevoDato[0]), len(array_train[0]))
  columna = []
  for i in range(len(array_train[0])):
    col = []
    for j in range(len(array_train)):
      col.append(array_train[j][i])
    print(titles[i], col)
  print()


  print("\ngenerando por columan el test")
  # print(len(nuevoDato[0]), len(array_test[0]))
  columna = []
  for i in range(len(array_test[0])):
    col = []
    for j in range(len(array_test)):
      col.append(array_test[j][i])
    print(titles[i], col)
  print()
