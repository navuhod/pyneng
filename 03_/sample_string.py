#tunnel = """
#interface Tunnel0
#ip address 10.10.10.1 255.255.255.0
#ip mtu 1416
#ip ospf hello-interval 5
#tunnel source FastEthernet1/0
#tunnel protection opsec profile DMVPN
#"""
#print(tunnel)

# строки то УПОРЯДОЧЕННЫЙ тип данных, позволяющий обращаться к символам в строке по номеру, начиная с нуля
strok = 'абвгдежзиклмнопрстуфхцчшыэюя'
print('пример строки набранной по-символьно с переменной strok="абвгдежзиклмнопрстуфхцчшыэюя":', strok[17]+strok[-4], end=' ')
print(strok[12]+strok[8]+strok[9]+strok[8]+strok[-11]+strok[0], end=' ')
print(strok[25]+strok[-11]+strok[13], end=' ')
print(strok[-11]+strok[13]+strok[6]+strok[5], end=' ')
print(strok[11]+strok[13]+strok[6]+strok[5]+strok[-5]+'ь')
print()
print('напечатанной вот таким "диким" способом: '), print('''print('пример строки набранной по-символьно с переменной strok="абвгдежзиклмнопрстуфхцчшыэюя":', strok[17]+strok[-4], end=' ')
print(strok[12]+strok[8]+strok[9]+strok[8]+strok[-11]+strok[0], end=' ')
print(strok[25]+strok[-11]+strok[13], end=' ')
print(strok[-11]+strok[13]+strok[6]+strok[5], end=' ')
print(strok[11]+strok[13]+strok[6]+strok[5]+strok[-5]+'ь')''')