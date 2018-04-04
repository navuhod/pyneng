# строки - неизменяемый тип данных, потому все методы, которые преобразуют строку возвращают
# новую строку, а исходная остается неизменной
# методы upper(), lower, swapcase(), capitalize() выполняют преобразование регистра строки:
print('методы upper(), lower, swapcase(), capitalize()','-'*50)
strok1 = 'FastEthernet'
strok2 = 'tunnel 0'
print("вид переменных:", "\t"*5,strok1, strok2, sep=" ")
print("переменные измененные методами:", "\t"*5,strok1.upper(), strok1.lower(), strok1.swapcase(), strok2.capitalize(), sep=" ")

# следует не забывать преобразования приcваивать новой переменной поскольку метод
# возвращает знаение в новой строке, иначе можно потерять результат
print("вид переменных после применения методов:", "\t"*5, strok1, strok2, sep=" ")
print()

# метод count() используют для подсчета количества непересекающихся вхождений подстроки в строковой переменной
print('count()', '-'*90)
strok1 = 'Hello, hello, hello, hello'
print('значение переменной:', strok1)
print('считаем длинну строки в символах используя метод len():', len(strok1))
print('считаем hello:', strok1.count('hello'))
print('считаем ello:', strok1.count('ello'))
print('считаем l:', strok1.count('l'))
print()

# метод find() возвращает позицию на которой находится первый символ построки-аргумента
print('find()', '-'*90)
strok1 = 'interface FastEthernet0/1'
print('вид переменной:', strok1, sep='\t')
print('''при использовании методов <имя_переменной>.find("Fast") и <имя_переменной>[<имя_переменной>.find("Fast")::]
получим соответствующие результаты: ''', strok1.find('Fast'), ' и ', strok1[strok1.find('Fast')::], sep='')
print()

# методы startswith() и endswith() проверяют начинается ли/заканчивается ли строка на определенные символы
# результат метода True или False
print('-'*100)
strok1 = 'FastEthernet0/1'
print('методы startswith() и endswith() проверяют начало и конец строки "', strok1, '" на заданные', sep='')
print('в аргументе символы, возвращая логические true/false в качестве результата')      
print(strok1.startswith('Fast'), strok1.startswith('fast'), strok1.endswith('0/1'), strok1.endswith('0/2'), sep='\t')
print()

# замена последовательности символов на другую последовательность - метод replace()
print('метод replace()', '-'*85)
strok1 = 'FastEthernet0/1'
print('переменную', strok1, 'метод replace("Fast", "Gigabit") меняет на', strok1.replace('Fast', 'Gigabit'))
print('-'*100)

# при открытии файла последовательно считывается каждая строка из файла, содержащая,
# как правило, различные спецсимволы, для удаления которых используется метод strip().
# по умолчанию метод убирает whitespace символы - это \t\n\r\f\v
strok1 = '\n\tFastEthernet0/1\n'
print('переменная "\\n\\tFastEthernet0/1\\n" до ...', strok1, '''
... и после использования метода strip():''', strok1.strip())
print('-'*100)

# методу strip можно передать как аргумент любые символ, тогда в начале и в конце строки
# будут удалены все символы совпадающие с аргументом метода strip
# для раздельного удаления символов в начале и в конце строки используются методы lstrip() и rstrip()
ad_metric = '[110/1045]'
print('переменная ad_metric содержит', ad_metric, 'и после метода strip("[]") выглядит', ad_metric.strip('[]'))
print('-'*100)

# метод split() разбивает строку на части, используя как разделитель значение указанное в аргументе
# по умолчанию, в качестве разделителя используется пробел
strok1 = ' switchport trunk allowed vlan 10,20,30,100-200\n'
print('''получая на вход переменную " switchport trunk allowed vlan 10,20,30,100-200\\n",
два метода strip и split последовательно превращают "<имя_переменной>.strip().split()" в список''')
l1st = strok1.strip().split()
print(strok1.strip().split()), print()
print('к последнему объекту списка: (', l1st[-1], ''') применяется метод split(), разделителем выступает (,)
результатом выполнения которого является список ''', l1st[-1].split(','), sep=''), print()
# по умолчанию split() разбивает строку, где элементы разделены ЛЮБЫМ количеством пробелов
sh_ip_int_br = 'FastEthernet0/0     15.0.15.1    YES manual up    up'
print('переменная "', sh_ip_int_br, '''" разбивается методом split()
на элементы, где результатом будет список ''', sh_ip_int_br.split(), sep='')
print('та же переменная разбиваемая при явном указании разделителя методом split(" ")'), print (sh_ip_int_br.split(' '))
print('-'*100)
