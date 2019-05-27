# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.

with open(r"C:\Users\vitaliy.prokudin\YandexDisk\Обучение\Python\HWGB_4\Les_4pwd.txt", "r") as f:
    ArrayPass = []
    # for line in f:
    #     ArrayPass.append(f.readline().split(";")[1])
    ArrayPass = [f.readline().split(';')[1] for line in f]
    # print(ArrayPass)
    PassCount = [ArrayPass.count(ArrayPass[i]) for i in range(len(ArrayPass))]
    # ArrayPass = [f.readline().split(';')[1] for line in f]
    # for i in range(10):
    #     # print(ArrayPass.count(ArrayPass[i]))
    # DictPass = {ArrayPass[i]: ArrayPass.count(ArrayPass[i]) for i in range(len(ArrayPass))}
    # r = open(r"C:\Users\vitaliy.prokudin\YandexDisk\Обучение\Python\HWGB_4\Result.txt", "w", encoding='​UTF-8')
    # for i in range(len(ArrayPass)):
    #     r.write(f"Пароль: {str(ArrayPass[i])} Кол.во={str(DictPass[ArrayPass[i]])}\n")
    #     # r.write(str(ArrayPass[i])+str(DictPass[ArrayPass[i]]))
    #     # # print(DictPass[ArrayPass[i]])
    #     # print(ArrayPass[i])
    # f.close()

    print(f"Пароль: {ArrayPass[PassCount.index(max(PassCount))]}Колличество повторений = {max(PassCount)}")


