# 1. Вычислить число c заданной точностью d
#     Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


def get_accuracy(number: str) -> int:
    calculation_pi = str(number)
    if '.' in calculation_pi:
        return abs(calculation_pi.find('.') - len(calculation_pi)) - 1
    else:
        return 0


def accuracy_Pi(accuracy: int) -> float:
    some_Pi = round(math.pi, accuracy)
    return some_Pi


number = input('Keep the accuracy of Pi: ')

print(f'Accuracy = 10^(-{get_accuracy(number)})')

try:
    number = int(get_accuracy(number))
    print(accuracy_Pi(number))
except:
    print("Enter the precision from 10^{-1} to 10^{-10}")
