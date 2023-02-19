# Домашнее задание к занятию 1. Знакомство с Python
# pyfree-homeworks/1.md at main · netology-code/pyfree-homeworks (github.com)
# Напишите программу, которая последовательно запрашивает у пользователя Дату и Описание задачи, а затем выводит их через пробел.

# data_from_user = input("Введите дату: ")
# task_from_user = input("Введите задачу: ")
# print(data_from_user, task_from_user)

# Модифицируйте программу из задания 1 таким образом, чтобы запрос даты и задачи выполнялся трижды
# и после этого результаты выводились на экран построчно в формате: на одной строчке дата и задача через пробел.

# for i in range (1,4):
#     print(i)
#
#     data_from_user = input("Введите дату: ")
#     task_from_user = input("Введите задачу: ")
#     print(data_from_user, task_from_user)
#
# else:
#     print("End")
#     print(data_from_user, task_from_user)

counter = 1

while counter < 4:
    counter = counter + 1
    print(counter)
    data_from_user = input("Введите дату: ")
    task_from_user = input("Введите задачу: ")
    print(data_from_user, task_from_user)

