# деление int и float
print('деление int - 10 на 3 ', 10/3)
print('деление float - 10 на 3.0 ', 10/3.0)
# функция round позволяет округлять до нужного числа знаков
print('округление до 2 и 4 знаков', round(10/3.0, 2), round(10/3.0, 4))
# целая часть и остаток от деления
print (10 // 3, 'целая часть от деления 10 на 3')
print(10 % 3, 'это остаток от деления 10 на 3')
# функция int() позволяет воплнять конвертацию в тип int.
# во втором аргументе можно указывать систему счисления
a = input('введите значение ')
print(int(a), int(a, 2))
# модуль math
import math
print('использование функции math '), print(math.sqrt(9), math.sqrt(10), math.factorial(3), math.pi, sep='\n')
