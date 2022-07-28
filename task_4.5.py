# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

import os


def write_file(name, p_p):
    with open(name, 'w') as file:
        file.write(p_p)


def create_str(working_list: list) -> str:
    working_list = working_list[::-1]
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


def degree_polynomial(k: str) -> int:
    if 'x^' in k:
        i = k.find('^')
        deg = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        deg = 1
    else:
        deg = -1
    return deg


def ratio_polynomial(n: str) -> int:
    if 'x' in n:
        i = n.find('x')
        ratio = int(n[:i])
    return ratio


def parsing_polynomial(p_p: list) -> list:
    p_p = p_p[0].replace(' ', '').split('=')
    p_p = p_p[0].split('+')
    work = []
    length = len(p_p)
    degree = 0

    if degree_polynomial(p_p[-1]) == -1:
        work.append(int(p_p[-1]))
        length -= 1
        degree = 1
    dd = 1
    ii = length - 1

    while ii >= 0:
        if degree_polynomial(p_p[ii]) != -1 and degree_polynomial(p_p[ii]) == dd:
            work.append(ratio_polynomial(p_p[ii]))
            ii -= 1
            dd += 1
        else:
            work.append(0)
            dd += 1

    return work


path1 = os.path.join('documentation', 'task_4.4(polynomial(1)).txt')
path2 = os.path.join('documentation', 'task_4.4(polynomial(2)).txt')

with open(path1, 'r') as file:
    str1 = file.readlines()
with open(path2, 'r') as file:
    str2 = file.readlines()
print(f'The first polynomial: {str1}')
print(f'The second polynomial: {str2}')

working_list_1 = parsing_polynomial(str1)
working_list_2 = parsing_polynomial(str2)
print(f'1', working_list_1)
print(f'2', working_list_2)

longer = working_list_1 if len(working_list_1) >= len(working_list_2) else working_list_2
working_list_3 = [x + y for x, y in zip(working_list_1, working_list_2)] \
                 + longer[min(len(working_list_1), len(working_list_2)):]
print(f'3', working_list_3)

path3 = os.path.join('documentation', 'task_4.5(sum_polynomials).txt')
write_file(path3, create_str(working_list_3))

with open(path3, 'r') as file:
    str3 = file.readlines()
print(f'The final polynomial: {str3}')
