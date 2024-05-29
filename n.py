#Lista 8
#Zad. 1

# import numpy as np

# arr = np.arange(0,10)
# print(arr)
# new_arr = (5,5)
# print(np.resize(arr, new_arr))
#----------------------------------------------

# import numpy as np

# arr = np.arange(10,39,2)
# print(arr.shape)
# print(np.resize(arr, (2,4)))
# print(arr+2)
# print(arr*2)
# arr[arr%6==2] = 0
# print(arr)
#----------------------------------------------

# import numpy as np

# def change(A, x):
#     # Tworzymy kopię tablicy A, aby nie modyfikować oryginalnej
#     result = np.copy(A)
#     # Zastępujemy zera wartością x
#     result[result == 0] = x
#     return result

# # Przykład użycia
# A = np.array([[1, 0, 3], [0, 5, 0], [7, 0, 9]])
# x = 10
# changed_array = change(A, x)

# print("Oryginalna tablica A:")
# print(A)
# print("\nTablica po zastąpieniu zer wartością", x, ":")
# print(changed_array)
#----------------------------------------------
#Zad2 np
# import numpy as np

# A = np.array([[1,1,2],[2,1,0],[4,1,2]])
# B = np.array([[2,5,7],[2,8,0],[4,3,1]])
# print(A+B)
# print(A*B)
# print(np.dot(A,B))
# print(np.linalg.matrix_power(A, -1))
# print(np.transpose(A))
# print(A**5)
# print(np.linalg.matrix_power(A, 5))
# print(np.linalg.det(B))
# print(np.linalg.matrix_power(B, -3))

# C = np.array([[1],[2],[4]])
# D = np.array([[2,5,7]])

# print(C*D)
# print(D*C)
# print(np.dot(C,D))
# print(C+D)

# E = np.array([[1,5],[2,1]])
# F = np.array([[2,1],[2,8]])

# print(E/F)
# print(E//F)
# print(E%F)
#--------------------------------------
#Zadanie 3
# def oblicz_wzrost_produkcji(dane):
#     # Inicjalizacja pustej listy, która będzie przechowywać wyniki
#     wyniki = []
#     # Obliczanie wzrostu produkcji dla każdego państwa
#     for i in range(9):
#         wyniki.append((dane[0][i],(dane[2][i]/dane[1][i])*100))

#     return wyniki

# # Dane wejściowe
# dane = [
#     ["China", "Japan", "Germany", "USA", "South Korea", "India", "Brazil", "Mexico", "Spain", "Russia"],
#     [0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94],
#     [19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69]
# ]

# # Wywołanie funkcji i wyświetlenie wyników
# wyniki = oblicz_wzrost_produkcji(dane)
# for panstwo, wzrost in wyniki:
#     print(f"{panstwo}: {wzrost:.2f}%")
#____________________________________________________________
# dane = [["China", "Japan", "Germany", "USA", "South Korea", "India", "Brazil", "Mexico", "Spain", "Russia"],
#         [0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94],
#         [19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69]]

# for i in range(len(dane[0])):
#     if(min(dane[1]) == dane[1][i]):
#         print(f'Najmniej aut w 1999: {dane[0][i]}')
    
#     if(max(dane[1]) == dane[1][i]):
#         print(f'Najwięcej aut w 1999: {dane[0][i]}')

# print("-------------------------")

# for i in range(len(dane[0])):
#     if(min(dane[2]) == dane[2][i]):
#         print(f'Najmniej aut w 2014: {dane[0][i]}')
    
#     if(max(dane[2]) == dane[2][i]):
#         print(f'Najwięcej aut w 2014: {dane[0][i]}')
#____________________________________________________________
# def oblicz_wzrost_produkcji(dane):
#     wyniki = []
#     for i in range(len(dane[0])):
#         if dane[2][i]<dane[1][i]:
#             wyniki.append(dane[0][i])
#     return wyniki

# # Dane wejściowe
# dane = [
#     ["China", "Japan", "Germany", "USA", "South Korea", "India", "Brazil", "Mexico", "Spain", "Russia"],
#     [0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94],
#     [19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69]
# ]

# # Wywołanie funkcji i wyświetlenie wyników
# wyniki = oblicz_wzrost_produkcji(dane)
# for panstwo in wyniki:
#     print(panstwo)
#______________________________________
#Zadanie 4
# dane = [
#     ["Anna", 21, "K", 65, 179, "NIE"],
#     ["Zofia", 40, "K", 80, 179, "TAK"],
#     ["Sylwia", 13, "K", 64, 151, "NIE"],
#     ["Katarzyna", 31, "K", 69, 177, "TAK"],
#     ["Teresa", 34, "K", 74, 170, "NIE"],
#     ["Tomasz", 14, "M", 61, 157, "TAK"],
#     ["Cezary", 13, "M", 66, 151, "NIE"],
#     ["Zenon", 28, "M", 61, 153, "TAK"],
#     ["Filip", 20, "M", 69, 160, "NIE"],
#     ["Adrian", 15, "M", 77, 160, "TAK"]
# ]

#a)
# li = []
# for i in range(len(dane)):
#     li.append(dane[i][0])

# li.sort()
# print(li)
#b)
# li = []
# for i in range(len(dane)):
#     if dane[i][5] == "TAK":
#         li.append(dane[i][0])

# print(li)
#c)
# li = []
# for i in range(len(dane)):
#     if dane[i][2] == "K" and 20 < dane[i][1] < 30:
#         li.append(dane[i][0])
# print(li)
#d)...
#---------------------------------------------------------------
#Lista 9 
#Zadanie 1
# import pandas as pd
# import numpy as np

# inty = pd.Series([3, -5, 7, 4])
# stri = pd.Series(['s3f', 'fds', 'bcx', 'asd'])
# a = [1,2,3,4]
# a = pd.Series(a)
# print(a)
# inty = list(inty)
# print(inty)
# b = np.arange(1,10,2)
# b = pd.Series(b)
# print(b)
# stri = np.array(stri)
# print(stri)
#-------------------------
# inty1 = pd.Series([3, -5, 7, 4])
# inty2 = pd.Series([4, 7, -5, 3])
# print(inty1 + inty2, inty1 - inty2, inty1 * inty2, inty1 / inty2)
# Tworzenie serii danych z losowymi liczbami
# c = np.arange(-10,10,0.1)
# d = pd.Series(c).sample(n=10)
# print(c,d)
#-------------------------
# data = {'Country': ['Belgium', 'India', 'Brazil'],
#         'Capital': ['Brussels', 'New Delhi', 'Brasília'],
#         'Population': [11190846, 1303171035, 207847528]}
# frame = pd.DataFrame(data)
# print(frame)
# df = pd.DataFrame(data, columns=['Country', 'Population', 'Capital'])
# print(df)
#___________________________________
#b)
# my_list = [1, 32, -37, 91, 12, 11, -5]
# a = pd.DataFrame(my_list, columns=['numbers'])
# a_list =a['numbers'].tolist()
# print(a_list)
# my_dict = {'a' : [1, 3, 2], 'b' : [2, 5, 7], 'c' : [3, 4, 8], 'd' : [4, 10, 12]}
# b = pd.DataFrame(my_dict, columns=['a','b','c','d'])
# b = b.to_dict()
# print(b)
# my_array = np.array([[1, 2, 5],[-2, 3, 3], [5, 2, 6]])
# c = pd.DataFrame(my_array, columns=['a','b','c'])
# c = c.to_numpy()
# print(c)
# my_series = pd.Series ([1, 32, -37, 91, 12, 11, -5], index = ['a','b','c','d','e','f','g'])
# d = pd.DataFrame(my_series)
# d = d.squeeze()
# print(d)
#___________________________________
#c)
# dane = [[1, 2, 4, 5], [-3, 8, 0.5, 10], [2, -5, 7, 3]]
# df = pd.DataFrame(dane, index=['l1', 'l2', 'l3'], columns=['a', 'b', 'c', 'd'])
# print(df)
# Wyciągnięcie wartości z wiersza 'l2' i kolumny 'b' ----------------------------------
# element = df.at['l2', 'b']
# print(element)
# Sortowanie względem kolumny 'c' -----------------------------------------------------
# df_sorted = df.sort_values(by='c')
# print(df_sorted)
# # Zmiana kształtu -------------------------------------------------------------------
# df_pivot = df.pivot(index=['a', 'b', 'c'], columns='d')
# print(df_pivot)

#===================================

#zadanie 2
# df1 = pd.DataFrame([[2942,9840,2794,8891,8111,2933,8301,9125],[ 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz','Cezary', 'Zenon', 'Filip', 'Adrian'],[13, 31, 34, 14, 13, 28, 20, 15]]).T
# df1.columns = ['ID', 'Name','Age']
# # print(df1)
# weight = [65, 80, 64, 69, 74, 61, 66, 61]
# height = [179, 179, 151, 177, 170, 157, 151, 153]
# glasses = [False, True, False, True, False, True, False, True]
# df2 = pd.DataFrame([[2312,2336,2942,9840,2794,8891,8111,2933], ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon'],weight,height,glasses]).T
# df2.columns = ['ID','Name','W', 'H','Gl']
# print(df2)
#-        -        -         -
# df0 = pd.merge(df1,df2,on='ID',how='inner')
# print(df0)

# df01 = pd.merge(df1,df2,on='ID',how='outer')
# print(df01)
#-        -        -         -
# print(df0.sort_values(by='Name_x'))
#-        -        -         -
#stwórz tablice przechowuj¡ca imiona osób nosz¡cych okulary (kolejno±¢ w tej tablicy musi odpowiednio zachowa¢ kolejno±¢ z wyj±ciowej tablicy)
# df02 = df2[df2['Gl'] == True]
# tab = np.array(df02['Name'])
# print(tab)
#-        -        -         -
# stwórz tablice zawieraj¡ca imiona osób w wieku z przedziaªu lat [20, 30]
# df03 = df1[(df1['Age'] > 20) & (df1['Age'] < 30)]
# tab = np.array(df03['Name'])
# print(tab)
#-        -        -         -
# dodaj kolumn¡ z bmi dla wszystkich osób i wynik zapisz w tablicy (bmi = waga/wzrost^2)
# df2['bmi'] = (df2['W']) / (df2['H']**2)
# print(df2)
#-        -        -         -
# policz ±redni wiek i wy±wietl na konsoli
# import statistics as sts
# print(sts.mean(df1['Age']))
#-        -        -         -
# policz osobna ±redni bmi osób nosz¡cych i nienosz¡cych okulary i wy±wietl na konsoli.
# df_glasses = df2[df2['Gl'] == True]
# df_no_glasses = df2[df2['Gl'] == False]
# print(f'Średnie BMI osób z okularami: {sts.mean(df_glasses['bmi'])}\n')
# print(f'Średnie BMI osób bez okularów: {sts.mean(df_no_glasses['bmi'])}')
#-        -        -         -
# policz osobna ±redni wiek osób nosz¡cych i nienosz¡cych okulary i wy±wietl na konsoli.
# df_glasses = df0[df0['Gl'] == True]
# df_no_glasses = df0[df0['Gl'] == False]
# print(f'Średni wiek osób z okularami: {sts.mean(df_glasses['Age']):.2f}')
# print(f'Średni wiek osób bez okularów: {sts.mean(df_no_glasses['Age'])}')

#===================================

#zadanie 1 / LISTA 10
# f = open('tekst1.txt', 'r+', encoding="UTF-8")
# s= f.read()
# breakpoint()
# print(s)
# print(type(s))

# --------------------

#zadanie 2 (Ź l e  z r o b i o n e, przecież nie da genfromtxt na kol :), skip>>)
# import numpy as np

# def c_data(var):
#     return [x for x in var if x!='']

# data = np.genfromtxt('jajka2024.csv', delimiter=";", dtype=('|U16'), encoding="UTF-8")
# print(data)
#a)
# Wyodrębnienie ceny jaj
# ceny_jaj = data[1:,1]
# ceny_jaj = c_data(ceny_jaj)
# # Konwercja ceny jaj na liczby zmiennoprzecinkowe
# ceny_jaj_float = np.array([float(cena.replace(',', '.')) for cena in c_data])
# srednia_cena_jaj = np.mean(ceny_jaj)
# print(f"Średnia cena jaj wynosi: {srednia_cena_jaj:.2f} zł")

#b)
# ceny_jaj = data[1:,1]
# miasta = data[0:,0]
# miasta = c_data(miasta)
# print(miasta)

# ceny_jaj = data[1:,1]
# ceny_jaj = c_data(ceny_jaj)
# print(ceny_jaj)
# ceny_jaj_float = np.array([float(cena.replace(',', '.')) for cena in ceny_jaj])
# max_cena_jaj = max(ceny_jaj_float)
# min_cena_jaj = min(ceny_jaj_float)
# print(min_cena_jaj, max_cena_jaj)

# --------------------

#zadanie 3
# import pandas as pd
# data = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='UTF-8')
# data2 = data.stack()
# data3 = data2.str.replace(',', '.').astype('float')
# srednia = data3.mean()
# minCena = data3.min()
# maxCena = data3.max()
# print(data3[data3 == minCena])
# print(data3[data3 == maxCena])

# --------------------

#zadanie 4
import matplotlib.pyplot as plt
import numpy as np

#1)
# x = [0, 1, 2, 3]
# y1 = [3, 8, 1, 10]
# y2 = [6, 2, 7, 11]
# plt.plot(x, y1, label='linear')
# plt.plot(x, y2, label='linear')
# plt.show()

#2)
# x = [7, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# y1 = [30, 28, 50, 48, 100, 48, 40, 45, 20, 30]
# y2 = [89, 90, 70, 89, 100, 80, 89, 100, 80, 35]
# plt.scatter(x, y2, c='red', marker="o", label='girls')
# plt.scatter(x, y1, c='blue', marker="o", label='boys')
# plt.xlabel('Grades Range')
# plt.ylabel('Grades Scored')
# plt.title("scatter plot")
# plt.legend()
# plt.show()

#3)

# data = [[15, 30, 1, 7, 23],
#         [28, 6, 16, 5, 10],
#         [29, 3, 24, 25, 16]]
# X = np.arange(5)

# plt.bar(X + 0.00, data[0], color='r', width=0.25, label="IT")
# plt.bar(X + 0.25, data[1], color='g', width=0.25, label="ECE")
# plt.bar(X + 0.50, data[2], color='b', width=0.25, label="CSE")
# labelsbar = np.arange(2015, 2020)
# plt.xticks(X + 0.25, labelsbar)
# plt.xlabel('Branch')
# plt.ylabel('Students passed')
# plt.legend()
# plt.show()