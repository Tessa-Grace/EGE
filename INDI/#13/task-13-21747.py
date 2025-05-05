from ipaddress import *

ip_net = ip_address('84.23.84.0')
ip_host = ip_address('84.23.84.23')

res = []
for mask in range(33):
    net = ip_network(f'{ip_host}/{mask}', False)
    if net.network_address == ip_net:
        byte = [int(x) for x in str(net.netmask).split('.')]
        res.append(sum(byte[2:]))

print(max(res))

# otvet: 479