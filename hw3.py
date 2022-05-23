# # Задание №1
#
# numb = input("напишите число : ")
# num_b = {
#     'one': "один",
#     'two': "два",
#     'three': "три",
#     'four': "четыре",
#     'five': "пять",
#     'six': "шесть",
#     'seven': "семь",
#     'eight' : "восем",
#     'nine' : "девять",
#     'ten' : "десять"
#          }
# print(f'{num_b[numb]}')
#
# # Задание 2
# def thesaurus(*args) -> dict:
#     resoult = {}
#     for name in args:
#         key = name[0].capitalize()
#         if key not in resoult:
#             resoult[key] = []
#         resoult[key].append(name)
#     return resoult
#     dict_out = {}  # результирующий словарь значений
#     return dict_out
#
# print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# # Задание 3
# import random
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#
# def get_jokes(count: int) -> list:
#     """Возвращает список шуток в количестве count"""
#     for _ in range(len(nouns)):
#         random_index = random.choice(nouns)
#         random_index_1 = random.choice(adverbs)
#         random_index_2 = random.choice(adjectives)
#         jokes = f'{random_index} {random_index_1} {random_index_2}'
#         print(jokes)
#     list_out = ["здесь собранные шутки"]
#     return list_out
#
# print(get_jokes(2))
# print(get_jokes(10))


# """Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы"""
# def get_jokes_adv(jokes, flag = False) -> list:
#
#         return []
