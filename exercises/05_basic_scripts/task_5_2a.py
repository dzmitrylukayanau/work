# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

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

ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(int(ipa[0]), int(ipa[1]), int(ipa[2]), int(ipa[3]))
ip_bin_netw = ip_bin[0:mask] + '0' * mask0
ip_fio = ip_bin_netw[0:8]
ip_so = ip_bin_netw[8:16]
ip_to = ip_bin_netw[16:24]
ip_fo = ip_bin_netw[24:]
ip_bin_all = ip_fio + '.' + ip_so + '.' + ip_to + '.' + ip_fo
ip_bin_all = ip_bin_all.split('.')

print(f'''
Network:
{int(ip_bin_all[0], 2):<8} {int(ip_bin_all[1], 2):<8} {int(ip_bin_all[2], 2):<8} {int(ip_bin_all[3], 2):<8}
{ip_fio} {ip_so} {ip_to} {ip_fo}''')

print(f'''
Mask:
/{mask}
{int(all_mask[0], 2):<8} {int(all_mask[1], 2):<8} {int(all_mask[2], 2):<8} {int(all_mask[3], 2):<8}
{first_oct} {sec_oct} {third_oct} {forth_oct}
''')


