
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами


import os
import time

n = int(input("Введите размер квадратной матрицы: "))
matr = []
count = 1
for i in range(n):
    matr.append([0] * n)

for i in range(n//2):
    for j in range(i, n - 1 - i):
        matr[i][j] = count
        count += 1
    for j in range(i, n - 1 - i):
        matr[j][n - 1 - i] = count
        count += 1
    for j in range(n - 1 - i, i, -1):
        matr[n - 1 - i][j] = count
        count += 1
    for j in range(n - 1 - i, i, -1):
        matr[j][i] = count
        count += 1
if n % 2 == 1:
    matr[n//2][n//2] = count

print("Подождите мы генерим вашу матрицу")
time.sleep(3)

for row in matr:
    print(row)

os.system("pause")