# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import os


def is_int(str: str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False


def input_list_int_numbers(str_in) -> list:
    list_dirty = str_in.split(' ')
    num_list = []
    for elem in list_dirty:
        if is_int(elem):
            num_list.append(int(elem))
    return num_list


def get_unique_numbers(num: list) -> list:
    list_of_unique_numbers = []
    unique_numbers = set(num)

    for num in unique_numbers:
        list_of_unique_numbers.append(num)

    return list_of_unique_numbers


path = os.path.join('documentation', 'task_4.3(num_list).txt')

with open(path, 'r') as file:
    str_in = file.readline()

print(str_in)
print(input_list_int_numbers(str_in))
print(get_unique_numbers(input_list_int_numbers(str_in)))
