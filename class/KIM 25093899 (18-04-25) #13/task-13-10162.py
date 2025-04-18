from ipaddress import ip_network, ip_address

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address == net2.network_address:
        if ip1 not in (net1.network_address, net1.broadcast_address): # проверка, что это не адрес сети и не широковещательный
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(net1.netmask)
# otvet:
# 0.0.0.0
# 128.0.0.0
# 192.0.0.0
# 224.0.0.0
# 240.0.0.0
# 248.0.0.0
# 252.0.0.0
# 254.0.0.0
# 255.0.0.0
# 255.128.0.0
# 255.192.0.0
# 255.224.0.0
# 255.240.0.0
# 255.248.0.0
# 255.252.0.0
# 255.254.0.0
# 255.255.0.0
# 255.255.128.0
# 255.255.192.0
# 255.255.224.0 <- наибольший третий байт = 224
