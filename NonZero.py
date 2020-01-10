#13 задание: Дан массив из 10 чисел. Подсчитать количество не нулевых элементов массива.
import numpy as np

n = 10

list = [int(input('Введите элемент массива ')) for i in range(n)]

count_nz=np.count_nonzero(list)

print ("Количество нулевых элементов: ", n-count_nz)
print("Количество ненулевых элементов: ", count_nz)

