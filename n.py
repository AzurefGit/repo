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
# import matplotlib.pyplot as plt
# import numpy as np

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

#4)
# # Dane
# sizes = [26.5, 16.2, 30.3, 26.2]
# labels = ['Python', 'C++', 'Ruby', 'Java']
# colors = ['yellow', 'g', 'm', 'c']
# explode = (0.1, 0, 0, 0)  # Wyróżnienie segmentu Kategoria B

# # Tworzenie wykresu kołowego
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# # Dodanie tytułu
# # plt.title('Przykład wykresu kołowego')

# # Równomierne skalowanie osi X i Y, aby koło było okrągłe
# plt.axis('equal')

# plt.show()

#5)
# # Dane przykładowe
# category_1_data = [750,850,930,990,1050] #i tak dalej w następnych przykładach...
# category_2_data = np.random.normal(820, 40, 100)
# category_3_data = np.random.normal(880, 20, 100)
# category_4_data = np.random.normal(830, 25, 100)
# category_5_data = np.random.normal(870, 35, 100)
# print(category_1_data)
# data = [category_1_data, category_2_data, category_3_data, category_4_data, category_5_data]

# plt.boxplot(data,)
# plt.axhline(y=790, color='r', linestyle='-', label='true speed')
# plt.ylabel('Speed of light (km/s minus 299,000)')
# plt.xlabel('Experiment No.')

# # plt.title('Wykres pudełkowy prędkości światła')
# # plt.legend()
# plt.show()

#6)
# -----------------------?

#=====================================

#Lista 9 
#Zadanie 1
# w pllikach


#Zadanie 2
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Wczytanie danych
# penguins = sns.load_dataset("penguins")
# penguins = penguins.dropna()
# # Przygotowanie mapy kolorów i kształtów
# color_map = {'Male': 'blue', 'Female': 'red'}
# shape_map = {'Adelie': 'o', 'Chinstrap': 's', 'Gentoo': 'D'}

# # Tworzenie nowej figury i osi
# fig, ax = plt.subplots()

# # Iteracja po każdym wierszu danych i rysowanie punktu
# for idx, row in penguins.iterrows():
#     ax.scatter(row['bill_length_mm'], row['bill_depth_mm'], color=color_map[row['sex']], 
#                s=row['body_mass_g']/50, marker=shape_map[row['species']])

# # Ustawienie etykiet osi
# ax.set_xlabel('Długość dzioba (mm)')
# ax.set_ylabel('Szerokość dzioba (mm)')

# # Wyświetlenie wykresu
# plt.show()

#-------------------------------

#Zadanie 3
# a)
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd

# iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# # Tworzenie nowej figury i osi dla wykresów punktowych
# fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# # Wykresy punktowe
# sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', ax=axs[0])
# sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', ax=axs[1])
# # Wykresy catplot
# sns.catplot(data=iris, x='species', y='sepal_length')
# sns.catplot(data=iris, x='species', y='sepal_width')
# sns.catplot(data=iris, x='species', y='petal_length')


# # Wyświetlenie wykresu
# plt.tight_layout()
# plt.show()

# b)
# import seaborn as sns
# import pandas as pd

# # Wczytanie danych
# iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# # Rysowanie pairplot
# sns.pairplot(iris, hue='species')
# plt.show()

#=================================
#Lista 12
#Zadanie 1
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-4, 4, 100)
# y = np.sin(x)
# y1 = 2*np.sin(x)
# y2 = np.sin(2*x)
# plt.plot(x, y2, 'blue', linestyle="-", label="sinx")
# plt.plot(x, y1, 'red', linestyle=":", label="2sin(x)")
# plt.plot(x, y, 'green', linestyle="--", label="sin(2x)")
# plt.legend(title='Wykres')
# plt.show()

# Zadanie 2 -----------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
# import math
# a)
# x = np.linspace(-10, 10, 100)
# y = 1/(1+x**2)
# plt.plot(x, y, 'green', linestyle="-", label="1/(1+x^2)")
# plt.legend(title='Wykres')
# plt.show()
# b)
# x = np.linspace(0, 4, 100)
# y1 = x**2
# y2 = math.e**x
# y3 = x**x
# plt.plot(x, y1, 'cyan', linestyle="-", label="x^2")
# plt.plot(x, y2, 'green', linestyle="--", label="e^x")
# plt.plot(x, y3, 'magenta', linestyle="-.", label="x^x")
# plt.legend(title='Wykresy')
# plt.show()
# c)
# x = np.linspace(0, 4, 100)
# y1 = x**2
# y2 = math.e**x
# y3 = x**x
#
# fig, [ax, ax1, ax2] = plt.subplots(nrows=3, ncols=1)
# ax.plot(x, y1, c='green', linestyle="--")
#
# ax.set_xlim([0, 3])
# ax.set_ylim([0, 20])
# ax1.plot(x, y2, c='red', linestyle=":")
#
# ax1.set_xlim([0, 3])
# ax1.set_ylim([0, 20])
# ax2.plot(x, y3, c='cyan', linestyle="-")
#
# ax2.set_xlim([0, 3])
# ax2.set_ylim([0, 20])
# fig.legend([ax, ax1, ax2], title="Wykres", labels=["x^2", "e^x", "x^x"], loc="upper center")
#
# plt.show()

# Zadanie 3
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# a)
# def sinplot(flip=1):
#     x = np.linspace(0, 14, 100)
#     for i in range(1, 5):
#         plt.plot(x, np.sin(x + i* .5)*(7 - i)* (flip))
# sns.set_style("whitegrid")
# sns.set_palette("husl")
# sinplot()
# print(sns.axes_style())
# plt.show()
# b)
# x = np.linspace(-2, 2, 100)
# x_sqrt = np.linspace(0, 2, 100)
# y_x = x
# y_x2 = x**2
# y_x3 = x**3
# y_sqrt = np.sqrt(x_sqrt)
# y_sqrt3 = np.cbrt(x_sqrt)
# sns.set_style("darkgrid")
# plt.figure(figsize=(8, 6))
# plt.plot(x, y_x)
# plt.plot(x, y_x2)
# plt.plot(x, y_x3)
# plt.plot(x_sqrt, y_sqrt)
# plt.plot(x_sqrt, y_sqrt3)
# plt.show()

# Zadanie 4
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import matplotlib.ticker as mtick

# glue = sns.load_dataset("glue")
# # print(glue)

# glue_df = sns.catplot(
# data= glue,
# kind="violin",
# x = 'Year',
# y ='Score',
# hue = 'Encoder',
# col = 'Encoder',
# row = 'Year',
# height=3,
# aspect = 1.5,
# palette=sns.color_palette(['green', 'orange']))

# glue_df.set_axis_labels('Year', 'Scores')
# plt.show()

# Więcej nie wykminię :P ,  K O N I E C
#------------------------------#
#pip install -m requirements.txt <- instalacja ręczna w terminalu requirements.txt
