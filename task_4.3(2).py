# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


def get_unique_numbers(numbers: list) -> list:
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


num_list = list(map(int, input('Enter the desired item positions separated by a space --> ').split()))
print(get_unique_numbers(num_list))
