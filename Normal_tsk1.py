 # Задание-1:
# # Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# # произвольными целыми цифрами, в результате в файле должно быть
# # 2500-значное произвольное число.
# # Найдите и выведите самую длинную последовательность одинаковых цифр
# # в вышезаполненном файле.

import random
import os

def Generation_numbers(Numbers):
    file = []
    for i in range(Numbers):
        file.append(random.randint(0,9))
    return ' '.join([str(i) for i in file])

def max_queue(Numbers):
    queue_file = Numbers.split(" ")
    queue_file = [int(i) for i in queue_file ]
    max_sequence = 0
    max_sequence_number = None
    last = 0
    count = 0
    for num in queue_file:
        if last == num:
            count += 1
        else:
            count = 1

        if count > max_sequence:
            max_sequence = count
            max_sequence_number = last

        last = num

    return max_sequence, max_sequence_number




with open(r"C:\\Users\\vitaliy.prokudin\\YandexDisk\\Обучение\\Python\\HWGB_4\\queue.txt", "w") as f:
    Numbers = Generation_numbers(int(input("Input number: ")))
    print(max_queue(Numbers))
    f.write(Numbers)
