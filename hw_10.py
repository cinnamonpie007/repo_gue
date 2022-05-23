# з1
# from typing import List
#
#
# class Matrix:
#     def __init__(self, matrix: List[List[int]]):
#         self.matrix = matrix
#
#     def __str__(self):
#         for row in self.matrix:
#             for i in row:
#                 print(f"{i:4}", end="")
#             print()
#         return ''
#
#     def __add__(self, other):
#         for i in range(len(self.matrix)):
#             for i_2 in range(len(other.matrix[i])):
#                 self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
#         return Matrix.__str__(self)
#
#
# if __name__ == '__main__':
#     first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
#     second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
#     print(first_matrix)
#     """
#     | 1 2 |
#     | 3 4 |
#     | 5 6 |
#     """
#     print(first_matrix + second_matrix)
#     """
#     | 7 7 |
#     | 7 7 |
#     | 7 7 |
#     """
#     fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
#     """
#     Traceback (most recent call last):
#       ...
#     ValueError: fail initialization matrix
#     """

# з2
# from abc import ABC, abstractmethod
#
#
# class Clothes:
#
#     def __init__(self, param):
#         self.param = param
#
#     @property
#     def calculate(self):
#         return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'
#
#     def abstract(self):
#         return 'абстракт'
#
# class Coat(Clothes):
#
#     @property
#     def calculate(self):
#         size = self.param / 6.5 + 0.5
#         return f'Для пошива пальто нужно: {size :.2f} ткани'
#
#     def abstract(self):
#         return 'абстракт'
#
#
# class Costume(Clothes):
#
#     @property
#     def calculate(self):
#         height = 2 * self.param + 0.3
#         return f'Для пошива костюма нужно: {height :.2f} ткани'
#
#     def abstract(self):
#         pass
#
#
# if __name__ == '__main__':
#     coat = Coat(45.0)
#     costume = Costume(3)
#
#     print(coat.calculate)  # 7.42
#     print(costume.calculate)  # 6.3


# з3

# class Cell:
#
#     def __init__(self, cells: int):
#
#         self.__cells = cells
#
#     def make_order(self, number: int) -> str:
#         """ ordering cells to cube the size eq split_cell*split_cell """
#
#         if number == 0:
#             raise ValueError("can't split cells by 0")
#
#         if number >= self._get_size():
#             return self._get_cells()
#
#         size = self._get_size()
#
#         return "".join([f"{x}\n" if i % number == 0 and i != size  else x
#                         for i, x in enumerate(self._get_cells(), start=1)])
#
#     def __add__(self, other: 'Cell'):
#         return Cell(self._get_size() + other._get_size())
#
#     def __sub__(self, other: 'Cell'):
#         if self._get_size() < other._get_size():
#             raise ValueError("cells can't be < 0")
#
#         return Cell(self._get_size() - other._get_size())
#
#     def __mul__(self, other: 'Cell'):
#         return Cell(self._get_size() * other._get_size())
#
#     def __floordiv__(self, other: 'Cell'):
#         return Cell(self._get_size() // other._get_size())
#
#     def _get_cells(self) -> str:
#         return str(self).replace("Cell(", "").replace(")", "")
#
#     def _get_size(self) -> int:
#         return self._get_cells().count("*")
#
#     def __str__(self) -> str:
#         return f"Cell({'*'*self.__cells})"
#
#
#
#
# if __name__ == '__main__':
#     cell_1 = Cell(15)
#     cell_2 = Cell(10)
#     cell_3 = Cell(3)
#
#     print(cell_1.make_order(10))
#     """
#     **********
#     *****
#     """
#
#     sum_cell = cell_2 + cell_3
#     print(sum_cell.make_order(6))
#     """
#     ******
#     ******
#     *
#     """
#
#     sub_cell = cell_1 - cell_3
#     print(sub_cell.make_order(6))
#     """
#     ******
#     ******
#     """
#
#     mul_cell = cell_2 * cell_3
#     print(mul_cell.cells)  # 30
#
#     floordiv_cell = cell_2 // cell_3
#     print(floordiv_cell.cells)  # 3
#
#     truediv_cell = cell_1 / cell_2
#     print(truediv_cell.cells)  # 1
#
#     try:
#         cell_3 - cell_2
#     except ValueError as err:
#         print(err)  # недопустимая операция
#
#     try:
#         cell_1 * 123
#     except TypeError as err:
#         print(err)  # действие допустимо только для экземпляров того же класса