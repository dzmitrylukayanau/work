# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Ведите ip адрес и маску в формате ip/mask: ')

ip_split = ip.split('.')
 
ip_last = ip_split.pop(-1)

ip_last = ip_last.split('/')

ip_addr =  '.'.join(ip_split) + '.' + ip_last[0]

ipa = ip_addr.split('.')

mask = int(ip_last[1])

mask0 = 32 - mask

onezero_mask = '1' * mask + '0' * mask0

first_oct = onezero_mask[0:8]
sec_oct = onezero_mask[8:16]
third_oct = onezero_mask[16:24]
forth_oct = onezero_mask[24:]
all_mask = first_oct + '.' + sec_oct + '.' + third_oct + '.' + forth_oct
all_mask = all_mask.split('.')

#print(ip_addr)
#print(mask)
#print(mask0)
#print(ipa)
#print(onezero_mask)
#print(all_mask)

print(f'''
Network:
{int(ipa[0]):<8} {int(ipa[1]):<8} {int(ipa[2]):<8} {int(ipa[3]):<8}
{int(ipa[0]):08b} {int(ipa[1]):08b} {int(ipa[2]):08b} {int(ipa[3]):08b}''')

print(f'''
Mask:
/{mask}
{int(all_mask[0], 2):<8} {int(all_mask[1], 2):<8} {int(all_mask[2], 2):<8} {int(all_mask[3], 2):<8}
{first_oct} {sec_oct} {third_oct} {forth_oct}
''')
