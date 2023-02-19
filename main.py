# Домашнее задание к занятию 1. Знакомство с Python
# pyfree-homeworks/1.md at main · netology-code/pyfree-homeworks (github.com)
# TASK 1 Напишите программу, которая последовательно запрашивает у пользователя Дату и Описание задачи, а затем выводит их через пробел.

# data_from_user = input("Введите дату: ")
# task_from_user = input("Введите задачу: ")
# print(data_from_user, task_from_user)

# TASK 2 Модифицируйте программу из задания 1 таким образом, чтобы запрос даты и задачи выполнялся трижды
# и после этого результаты выводились на экран построчно в формате: на одной строчке дата и задача через пробел.

# first try
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

# second try
# counter = 1
# while counter < 4:
#     counter = counter + 1
#     print(counter)
#     data_from_user = input("Введите дату: ")
#     task_from_user = input("Введите задачу: ")
#     print(data_from_user, task_from_user)

# TASK 2
# Declare th lists
user_data_list = []
user_task_list = []

counter = 1
while counter < 4:
    counter = counter + 1
    print(counter)

    user_data = input("Введите дату: ")
    user_task = input("Введите задачу: ")
    user_data_list.append(user_data)
    user_task_list.append(user_task)

#print(user_data_list)
#print(user_task_list)
print(user_data_list[0],user_task_list[0])
print(user_data_list[1],user_task_list[1])
print(user_data_list[2],user_task_list[2])

# merge lists
# sum_2 = numbers + data
# get the first element of the list, the first number of the list is 0
# first = strings[0]
# second = strings[1]

# TASK 3

