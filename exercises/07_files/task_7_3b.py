# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result={}
vlans = []
macs = []
interfaces = []

v = int(input('Enter VLAN number: '))

with open('CAM_table.txt') as f: 
    for line in f: 
        line = line.split() 
        if '----' in line: 
            continue 
        elif '-------------------------------------------' in line: 
            continue 
        elif line and line[1][0].isdigit() and line[1][1].isalpha():   
            vlan = line[0]  
            mac = line[1]  
            intf = line[3]
            vlans.append(int(vlan))
            macs.append(mac)
            interfaces.append(intf)
            result[intf]= {}
            result[intf]['vlan'] = vlan
            result[intf]['mac'] = mac  
        elif line and line[1][0].isalpha() and line[1][1].isdigit(): 
            vlan = line[0] 
            mac = line[1] 
            intf = line[3]
            vlans.append(int(vlan))
            macs.append(mac)
            interfaces.append(intf)
            result[intf]= {}
            result[intf]['vlan'] = vlan
            result[intf]['mac'] = mac  
        elif line and line[1][0].isdigit() and line[1][1].isdigit(): 
            vlan = line[0] 
            mac = line[1] 
            intf = line[3]
            vlans.append(int(vlan))
            macs.append(mac)
            interfaces.append(intf)
            result[intf]= {}
            result[intf]['vlan'] = vlan
            result[intf]['mac'] = mac

for key in result:
    if v == int(result[key]['vlan']):
        print('{:<10}{:20}{}'.format(v, result[key]['mac'], key))

