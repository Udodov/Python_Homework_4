# 1. Вычислить число c заданной точностью d
#     Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import os


def formula_Leibniz(repetitions: int) -> int:
    private = 1
    calculation = 0
    for i in range(repetitions):
        if i % 2 == 0:
            calculation += 4 / private
        else:
            calculation -= 4 / private
        private += 2
    return calculation


def get_accuracy(d: str) -> int:
    calculation_pi = str(d)
    if '.' in calculation_pi:
        return abs(calculation_pi.find('.') - len(calculation_pi)) - 1
    else:
        return 0


def accuracy_Pi(accuracy: int) -> float:
    some_Pi = round(formula_Leibniz(repetitions), accuracy)
    return some_Pi


path = os.path.join('documentation', 'task_4.1(acc_Leib).txt')

with open(path, 'r') as f:
    f.readline()
    repetitions = int(f.readline())

# repetitions = int(input('Enter the value of the number of terms in the series of the Leibniz formula '
#                     '(the more, the closer to Pi) 10^{6}, for example: '))

in_d = input('Enter the precision from 10^{-1} to 10^{-10} of Pi: ')

print(f'Accuracy = 10^(-{get_accuracy(in_d)})')

try:
    d = int(get_accuracy(in_d))
    print(accuracy_Pi(d))
except:
    print("Enter the precision from 10^{-1} to 10^{-10}")
