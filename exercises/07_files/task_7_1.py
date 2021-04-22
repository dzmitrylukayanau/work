# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
keys = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface'] 

with open('ospf.txt') as f:
    for line in f:
        line = line.split()
        if line:
            print(f''' 
                {keys[0]:<22} {line[1]:<22} 
                {keys[1]:<22} {line[2].strip('[]'):<22} 
                {keys[2]:<22} {line[4].rstrip(','):<22} 
                {keys[3]:<22} {line[5].strip(','):<22} 
                {keys[4]:<22} {line[6]:<22} 
                ''')                              

