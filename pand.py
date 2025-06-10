# import pandas as pd

# data = [50, 60, 70, 80, 90]
# s = pd.Series(data, index=['a', 'b', 'c', 'c', 'e'])
# s = pd.Series(data)
# print(s)

# zod = {"a": 50, "b": 60, "c": 70, "c": 80, "e": "A",10:5}
# s = pd.Series(zod)
# print(s)

# generate letters from a to z
# def generate_letters():
#     """Generate a list of lowercase letters from 'a' to 'z'."""
#     letters = []
#     print(ord('a'), ord('z'))
#     for i in range(ord('a'), ord('z') + 1):
#         letters.append(chr(i))
#     return letters

# print(generate_letters())

# print(s)
# print(s.head(3)) # grazina pirmus x elementu
# print(s.tail(3)) # grazina paskutinius x elementu
# print(s.size)
# print(s.shape) 
# print(s.dtypes) # grazina duomenu tipu sarasa
# print(s.values) # grazina numpy array su reiksmemis
# print(s.index) # grazina indeksa

# print(s['a']) # grazina reiksmes su indeksu 'c' 
# print(s["a":"d"]) # grazina reiksmes su indeksais 'c' ir 'e'
# print(s[['a', 'c']]) # grazina reiksmes su indeksais 'a' ir 'c'
# print(s.loc['a']) # grazina reiksme su indeksu 'a'
# print(s.iloc[1]) # grazina reiksme su indeksu 0

# print(s[s > 70])  # grazina reiksmes, kurios yra didesnes uz 70
# s[s > 70] = 0
# print(s)  # atnaujinta serija, kur reiksmes didesnes uz 70 pakeistos i 0

# s = s.add([10,15,19,20,25])
# print(s)  # atnaujinta serija, kur visos reiksmes padidintos 20

# print(s.mean())  # vidurkis
# print(s.to_numpy().std())
# print(s.std())


# import pandas as pd
# # create series with random values and some NaN values with at least 20 values
# import numpy as np
# # data = [50, 60, 70, 80, 90, np.nan, 110, 120, 130, 140, np.nan, 160, 170, 180, 190, np.nan, 210, 220, 230, 240, np.nan]
# # s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'])
# # print(s)
# # print(s.isna())  # grazina True, jei yra NaN reiksme

# # print(s.isna().sum())  # grazina kiek yra NaN reiksmiu
# # # print(s.dropna()) # grazina serija be NaN reiksmiu
# # print(s.fillna(s.mean()))  # pakeicia NaN reiksmes i 100
# # series string operations
# s = pd.Series(['apple', 'banana', 'fig', 'date', 'elderberry', 'fig', 'grape'])
# # print(s)
# # print(s.str.upper())  # grazina serija su visomis reiksmeis didziosiomis raidemis
# # print(s.str.contains('a'))  # grazina serija su True, jei reiksmeje yra 'a'
# print(s.value_counts())  # grazina serija su reiksmeis ir ju kiekiais
# print(s.unique()) # grazina unikaliu reiksmiu sarasa
# print(s.nunique())  # grazina kiek yra unikaliu reiksmiu

# def multiply_by_two(x):
#     """Padvigubina skaiciu."""
#     if isinstance(x, (int, float)):
#         return x * 2
#     return x

# s= s.apply(lambda x: x * 2 if isinstance(x, (int, float)) else x)  # padvigubina visas reiksmes, kurios yra int arba float
# s = s.apply(multiply_by_two)  # padvigubina visas reiksmes, kurios yra int arba float
# print(s)
# # map values in series
# s = s.map({'apple': 'red', 'banana': 'yellow', 'fig': 'purple', 'date': 'brown', 'elderberry': 'black', 'grape': 'green'})
# print(s)  # pakeicia reiksmes pagal zodyna

# s.sort_values(inplace=True)  # surikiuoja serija pagal reiksmes
# print(s)  # atspausdina surikiuota serija


# s.sort_index(inplace=True)  # surikiuoja serija pagal indeksus
# print(s)  # atspausdina surikiuota serija pagal indeksus