# """задание №1"""
# def odd_nums(number: int) -> int:
#     """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
#     pass
#     for i in range(1, number + 1, 2):
#         # # 1.2
#         # return (i for i in range(1, number + 1, 2))
#         # # 1.1
#         # yield i
#         # print("next(odd_to_15)")
#
#
# n = 15
# generator = odd_nums(n)
# for _ in range(1, n + 1, 2):
#     print(next(generator))
# # next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration

# """"Задание 3"""
#
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
#
# def check_gen(tutors, klasses):
#
#     len_klasses = len(klasses)
#
#     return ((tut, klasses[i]) if i < len_klasses else (tutors, None)
#             for i, tut in enumerate(tutors))
#
#
# generator = check_gen(tutors, klasses)
# print(type(generator))
# for _ in range(len(tutors)):
#     print(next(generator))
# # next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration


# """"задание 4"""
#
# def get_numbers(src: list):
#     pass
#     return (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
#
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# print(*get_numbers(src))

# """"задание 5 """
# def get_uniq_numbers(src: list):
#     pass
#     numb = set()
#     for elem in src:
#         if not elem in numb:
#             numb.add(elem)
#         else:
#             numb.remove(elem)
#
#     return [x for x in src if x in numb]
#
#
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print(*get_uniq_numbers(src))


