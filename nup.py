# sarasas = [7,2,4,9,5] # [2, 4, 5, 7, 9] - 5 mediana

# sarasas = [9,1,7,3,5,4] # [1, 3, 4, 5, 7, 9] - 4.5 mediana

import numpy as np
# print(np.mean(sarasas))
# print(np.median(sarasas))

# sarasas = [7,2,4,9,5,4,9,5,2,3,5,7,700] # 100/5 = 20% | 20*3=60% # 
# print(np.mean(sarasas))

# print(np.std(sarasas))

sarasas = [5,47,38,63,42,20,27,180] # 10 - 80
# print(np.mean(sarasas))

# print(np.std(sarasas))

apatine_riba = np.mean(sarasas) - 2 * np.std(sarasas)
virsutinė_riba = np.mean(sarasas) + 2 * np.std(sarasas)

print(f"Apatinė riba: {apatine_riba}")
print(f"Viršutinė riba: {virsutinė_riba}")

# drop from list
sarasas = [x for x in sarasas if x >= apatine_riba and x <= virsutinė_riba]
print(f"Filtruotas sąrašas: {sarasas}")