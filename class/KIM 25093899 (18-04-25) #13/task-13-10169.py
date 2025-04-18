from ipaddress import ip_address, ip_network

ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address != net2.network_address:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(mask)
# otvet:
# 21 <- наименьшее кол-во единиц
# 22
# 23
# 24
# 25
# 26
# 27