# форматирование строк может быть использовано в ситуациях:
# - необходимо подставить значение в строку по определенному шаблону 
# - необходимо отформатировать вывод столбцами
# - надо конвертировать числа в двоичный формат

# существует два варианта форматирования строк:
# - методом format() (новый, РЕКОМЕНДОВАННЫЙ вариант)
# - с оператором % (старый вариант)
print("*"*12, "форматирование методом format()", "*"*12, '\n'*2)
print("interface FastEthernet0/{}".format('1'), '\n'*2)
# print("interface FastEthernet0/{}".format(input()))

# специальный символ {} указывает, куда подставится значение, которое передается методу format,
# при том каждая пара  фигурных скобок означает ОДНО место для подстановки.
# значения, подставляемые в фигурные скобки могут быть разного типа СТРОКА, ЧИСЛО или СПИСОК
print('{}'.format('10.1.1.1'), end='     '), print('{}'.format(100), end='     '), print('{}'.format([10, 1, 1, 1]))
print()

# с помощью форматирования можно выводить результат столбцами. в форматировании строк можно указывать
# какое количество знако-полей выделено на данные. если количество символов в данных меньше чем выделенное
# количество знако-полей, недостающие поля заполняются пробелами

# пример вывода данных столбцами одинаковой ширины по 15 знако-полей, с выравниванием по правой стороне 
vlan, mac, intf = ['100', 'aabb.cc80.7000', 'GiO/1']
print("{:>15} {:>15} {:>15}".format(vlan, mac, intf))
# пример вывода данных столбцами одинаковой ширины по 15 знако-полей, с выравниванием по лефой стороне 
print("{:15} {:15} {:15}".format(vlan, mac, intf))
print()

# шаблон для вывода может быть многострочным
mac_template = '''
MAC-adress:
{}
'''
print(mac_template.format(mac))

# с помошью форматирования можно влиять на формат отображение чисел
print("явно указываем количество знаков после запятой: {:.3f}".format(10.0/3))
print(" "*52+"^")
print("{"+":.3f}"+"_"*46+"|", '\n'*2)

# с помощью форматирования можно конверитровать числа в двоичный формат
print('{:b} {:b} {:b} {:b}'.format(192, 100, 1, 1))
# указать ширину столбцов в знаках
print('{:8b} {:8b} {:8b} {:8b}'.format(192, 100, 1, 1))
# и дополнить не полные разряды незначащими нулями вместо пробелов
print('{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1), '\n'*2)

# существует возможность поля шаблона оределять явным образом
print('{ip}/{mask}'.format(mask=24, ip='10.1.1.1'))
# и указывать индекс аргумента
print('{1}/{0}'.format(24, '10.1.1.1'), '\n'*2)

# возможность указания индекса аргумента позволяет избавиться от повторной передачи одних и тех же данных
# в примере октеты адреса передаются дважды, для отображения десятичного и во второй раз для двочного формата
ip_template = '''
IP address:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''
print(ip_template.format(192, 100, 1, 1, 192, 100, 1, 1))
# указав индексы значений, которые передаются етоду format можно избавиться от дублирования
ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(192, 100, 1, 1))


