from ipaddress import *

for mask in range(33):
    net = ip_network(f'192.168.32.160/{mask}', 0)
    print(net)

# 192.168.32.160/27
# 192.168.32.160/28
# 192.168.32.160/29
# 192.168.32.160/30
# 192.168.32.160/31
# 192.168.32.160/32

# сколько адресов с четным кол-вом единиц?
# 192.168.32.160/28
# 192.168.32.160/30
# 192.168.32.160/32

#otvet: 3