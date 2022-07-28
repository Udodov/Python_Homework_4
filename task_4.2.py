# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def list_multipliers(num: int) -> list:
    i = 2
    multipliers = []
    while num != 1:
        if num % i == 0:
            multipliers.append(i)
            num /= i
            i = 2
        else:
            i += 1
    return (multipliers)


number_N = int(input('Set a natural number: '))
print(list_multipliers(number_N))
