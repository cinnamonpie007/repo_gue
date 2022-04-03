# Задание 1
#
# num = int(input("введите секунды : "))
#
# sec = num % 86400
#
# min = sec // 60
#
# sec %= 60
#
# h = min // 60
#
# min %= 60
#
# day = num // 86400
#
# print(f"{day} дней {h} часов {min} мин {sec} секунд")

# Задание №3
# n = int(input('введите сколько процентов : '))
#
# proc_1 = n % 10
#
# if n == 1:
#     print(f'{n} процент')
#
# elif n == 10 or n == 11 or n == 12 or n == 13 or n == 14:
#     print(f'{n} процентов')
#
# elif proc_1 == 1:
#     print(f'{n} процент')
#
# elif n == 2 or n == 3 or n == 4:
#     print(f'{n} процента')
#
# elif proc_1 == 2 or proc_1 == 3 or proc_1 == 4:
#     print(f'{n} процента')
#
# else:
#     print(f'{n} процентов')

# С заданием №2 вышли сложности, так и не смог решить до конца

# number_list = [i**3 for i in range(1, 1001, 2)]
# print(number_list)
# num_2 = 0
# num_3 = 0
# num_4 = 0
# num_5 = 0
# num_6 = 0
# num_7 = 0
# num_8 = 0
# num_9 = 0
# num_10 = 0
# num_11 = 0
# for num_2 in number_list:
#     num_2 %= 10
#     # print(num_2)
# for num_3 in number_list:
#     num_3 %= 100
#     num_3 //= 10
#     # print(num_3)
# for num_4 in number_list:
#     num_4 %= 1000
#     num_4 //= 100
#     # print(num_4)
# for num_5 in number_list:
#     num_5 %= 10000
#     num_5 //= 1000
#     # print(num_5)
# for num_6 in number_list:
#     num_6 %= 100000
#     num_6 //= 10000
#     # print(num_6)
# for num_7 in number_list:
#     num_7 %= 1000000
#     num_7 //= 100000
#     # print(num_7)
# for num_8 in number_list:
#     num_8 %= 10000000
#     num_8 //= 1000000
#     # print(num_8)
# for num_9 in number_list:
#     num_9 %= 100000000
#     num_9 //= 10000000
#     # print(num_9)
# for num_10 in number_list:
#     num_10 %= 1000000000
#     num_10 //= 10000000
#     # print(num_10)
# for num_11 in number_list:
#     num_11 %= 10000000000
#     num_11 //= 100000000
#     # print(num_11)
# n = (num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, num_10, num_11)
# suma = 0
# for s, number_list in enumerate(n):
#     s = num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_8 + num_9 + num_10 + num_11
#     print(s)
