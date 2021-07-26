# -*- coding: utf-8 -*-
"""
Задание 9.2

Создать функцию generate_trunk_config, которая генерирует
конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  такого вида:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (список trunk_mode_template)

Функция должна возвращать список команд с конфигурацией на основе указанных портов
и шаблона trunk_mode_template. В конце строк в списке не должно быть символа
перевода строки.

Проверить работу функции на примере словаря trunk_config
и списка команд trunk_mode_template.
Если предыдущая проверка прошла успешно, проверить работу функции еще раз
на словаре trunk_config_2 и убедится, что в итоговом списке правильные номера
интерфейсов и вланов.


Пример итогового списка (перевод строки после каждого элемента сделан
для удобства чтения):
[
'interface FastEthernet0/1',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 10,20,30',
'interface FastEthernet0/2',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan 11,30',
...]


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':[10, 20]
         'FastEthernet0/14':[11, 21]
         'FastEthernet0/16':[17, 27]}
    trunk_template - список команд для порта в режиме trunk

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    result = []

    for intf, vlan in intf_vlan_mapping.items():
        result.append(f'interface {intf}')
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                vl_list = ",".join([str(vl) for vl in vlan])
                result.append('{} {}'.format(command, vl_list))
            else:
                result.append('{}'.format(command))
    return(result)

final = generate_trunk_config(trunk_config, trunk_mode_template)
print(final)

#for vl in vlans:
#    if len(vl_list) == 0:
#        vl_list = vl_list + str(vl)
#    else:
#        vl_list = vl_list + ', ' + str(vl)

