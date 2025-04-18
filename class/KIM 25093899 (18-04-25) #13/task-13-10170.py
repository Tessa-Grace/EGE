from ipaddress import ip_address, ip_network

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address != net2.network_address:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(net1.netmask)
# otvet:
# 255.255.240.0 <- мин третий байт 240
# 255.255.248.0
# 255.255.252.0
# 255.255.254.0
# 255.255.255.0
# 255.255.255.128
# 255.255.255.192
# 255.255.255.224
# 255.255.255.240