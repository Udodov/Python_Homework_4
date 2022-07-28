# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
#    Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 /// (K+1)*x^K + K*x^(K-1)+...+(K-?)*x^0 = 0

import os
import random


def create_str(working_list: list) -> str:
    result = ''

    if len(working_list) <= 1:
        result = 'the polynomial does not exist'

    else:
        for i in range(len(working_list)):
            if working_list[i] != 0:

                if (i != len(working_list) - 1) and (i != len(working_list) - 2):
                    result += f'{working_list[i]}x^{len(working_list) - i - 1}'
                    if working_list[i + 1] != 0:
                        result += ' + '

                elif i == len(working_list) - 2:
                    result += f'{working_list[i]}x'
                    if working_list[i + 1] != 0:
                        result += ' + '

                elif i == len(working_list) - 1:
                    result += f'{working_list[i]} = 0'

            else:
                if i != len(working_list) - 1:
                    result += ''
                    if working_list[i + 1] != 0:
                        result += ' + '
                else:
                    result += ' = 0'

    return result


k = random.randint(0, 10)
ratios_list = [random.randint(0, 101) for i in range(k + 1)]
# ratios_list = [3, 0, 3, 0, 5, 0]

print(ratios_list)
print(create_str(ratios_list))

path = os.path.join('documentation', 'task_4.4(polynomial(1)).txt')
with open(path, 'w') as equation:
    equation.write(create_str(ratios_list))
