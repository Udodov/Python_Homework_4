# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
#    Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os

import random
import itertools


def polynomial_str(degree: int, ratios_list: list) -> str:
    part = ['x^'] * (degree - 1) + ['x']
    list_tuple = [[a, b, c] for a, b, c in itertools.zip_longest(ratios_list, part, range(degree, 1, -1), fillvalue='')
                  if a != 0]

    for x in list_tuple:
        x.append(' + ')

    result = list(itertools.chain(*list_tuple))
    result[-1] = ' = 0'
    result = ''.join(map(str, result))

    return result


k = random.randint(0, 10)
ratio_list = list([random.randint(0, 101) for i in range(k + 1)])
# ratio_list = [3, 0, 3, 0, 5, 0]

print(ratio_list)
print(polynomial_str(k, ratio_list))  # print(polynomial_str(4, ratio_list))

# path = os.path.join('documentation', 'task_4.4(polynomial(2)).txt')
# with open(path, 'w') as equation:
#     equation.write(polynomial_str(k, ratio_list))  # equation.write(polynomial_str(4, ratio_list))
