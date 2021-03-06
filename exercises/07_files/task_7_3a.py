# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт:  Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result={}
vlans = []
macs = []
interfaces = []

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
#            print('{:10}{:20}{}'.format(vlan, mac, intf)) 
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

#print(sorted(vlans))
#print(macs)
#print(interfaces)
#print(result)

vlans = sorted(list(set(vlans)))

for v in vlans:
    for key in result: 
        if v == int(result[key]['vlan']): 
            print('{:<10}{:20}{}'.format(v, result[key]['mac'], key))
    
