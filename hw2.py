# Задание №1
# a = 15 * 3
# b = 15 / 3
# c = 15 // 2
# d = 15 ** 2
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# Задание №2

# def convert_list_in_str(list_in: list) -> str:
#     """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
#         списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
#         Формирует из списка результирующую строковую переменную и возвращает."""
#     my_list_1 = []
#     for word in my_list:
#         if word.isdigit():
#             my_list_1.extend(['"', word.zfill(2), '"'])
#         elif word[0] == '+' or word[0] == '-':
#             my_list_1.extend(['"', f'{word[0]}0{word[1:]}', '"'])
#         else:
#             my_list_1.append(word)
#
#     return ' '.join(my_list_1)
#
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# result = convert_list_in_str(my_list)
# print(result)

# задание 3
#
# def convert_name_extract(list_in: list) -> list:
#     """Извлекает имена из элементов и формирует список приветствий."""
#     for position in my_list:
#         print('Привет,', position.split()[-1].title(), '!')
#     return list_in
#
#
# my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# result = convert_name_extract(my_list)
# print(result)

# задание 4


# from random import uniform
# numbs = [57.8, 46.51, 97, 16.87, 13.07, 83, 12.15, 96.15, 100, 17]
#
# def transfer_list_in_str(list_in: list) -> str:
#     """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
#         формирует из них единую строковую переменную разделяя значения запятой."""
#     # numbs = [57.8, 46.51, 97, 16.87, 13.07, 83, 12.15, 96.15, 100, 17]
#     for price in numbs:
#         price = int(price)
#         rub = price
#         kop = (price - rub) * 100
#         print(f'{rub} рублей {kop:02.0f} копеек')
#     str_out = "здесь итоговая строка"
#     return str_out
#
#
# my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
# print(f'Исходный список: {my_list}')
# result_1 = transfer_list_in_str(my_list)
# print(result_1)
#
#
# def sort_prices(list_in: list) -> list:
#     """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
#     numbs.sort()
#     print(numbs)
#     return ["отсортированный результирующий список"]
#
#
# # зафиксируйте здесь информацию по исходному списку my_list
# result_2 = sort_prices(my_list)
# # зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
# print(result_2)
# #
# #
# def sort_price_adv(list_in: list) -> list:
#     """Создаёт новый список и возвращает список с элементами по убыванию"""
#     new_list = numbs
#     new_list.sort()
#     new_list.reverse()
#     print(new_list)
#     list_out = ["список элементов в списке по убыванию"]
#     return list_out
#
#
# result_3 = sort_price_adv(my_list)
# print(result_3)
#
#
# def check_five_max_elements(list_in: list) -> list:
#     """Проверяет элементы входного списка вещественных чисел и возвращает
#         список из ПЯТИ максимальных значений"""
#     numbs.sort()
#     numbs.reverse()
#     sort = numbs[0:5]
#     print(sort)
#     list_out = ["список из пяти самых больших элементов"]
#     return list_out
#
#
# result_4 = check_five_max_elements(my_list)
# print(result_4)

