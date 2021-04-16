# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-адрес в формате x.x.x.x: ')
ip_correct = False

while not ip_correct:
    if len(ip.split('.')) != 4:
        print('Неправильный IP-адрес\n')
        ip = input('Введите IP-адрес в формате x.x.x.x: ')
    elif ip.split('.')[0].isdigit() and ip.split('.')[1].isdigit() and ip.split('.')[2].isdigit() and ip.split('.')[3].isdigit():
        if 255 >= int(ip.split('.')[0]) >= 0 and 255 >= int(ip.split('.')[1]) >= 0 and 255 >= int(ip.split('.')[2]) >= 0 and 255 >= int(ip.split('.')[3]) >= 0:
            if 0 < int(ip.split('.')[0]) < 224:
                print('unicast')
                ip_correct = True
            elif 224 <= int(ip.split('.')[0]) <= 239:
                print('multicast')
                ip_correct = True
            elif ip == '255.255.255.255':
                print('local broadcast')
                ip_correct = True
            elif ip == '0.0.0.0':
                print('unassigned')
                ip_correct = True
            else:
                print('unused')
                ip_correct = True
        else:
            print('Неправильный IP-адрес\n')
            ip = input('Введите IP-адрес в формате x.x.x.x: ')
    else:
        print('Неправильный IP-адрес\n')
        ip = input('Введите IP-адрес в формате x.x.x.x: ')

