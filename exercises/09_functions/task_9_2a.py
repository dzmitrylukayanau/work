# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

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

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':[10, 20]
         'FastEthernet0/14':[11, 21]
         'FastEthernet0/16':[17, 27]}
    trunk_template - список команд для порта в режиме trunk

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    dic = {}
    final = {}

    for intf, vlan in intf_vlan_mapping.items():
        dic[f'interface {intf}'] = []
        for command in trunk_template:
            result = []
            if command.endswith('allowed vlan'):
                vl_list = ''
                for vl in vlan:
                    if len(vl_list) == 0:
                        vl_list = vl_list + str(vl)
                    else:
                        vl_list = vl_list + ',' + str(vl) 
                result.append('{} {}'.format(command, vl_list))
            else:
                result.append('{}'.format(command))
        for inter in dic.keys():
            final[inter] = result

    return(final)

final = generate_trunk_config(trunk_config, trunk_mode_template)
print(final)


