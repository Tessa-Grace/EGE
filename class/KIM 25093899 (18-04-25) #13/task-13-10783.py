from ipaddress import ip_address, ip_network

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')

for mask in range(33):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address == net2.network_address:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.network_address, net2.broadcast_address):
                print(net1.num_addresses)
# otvet:
# 4294967296
# 2147483648
# 1073741824
# 536870912
# 268435456
# 134217728
# 67108864
# 33554432
# 16777216
# 8388608
# 4194304
# 2097152
# 1048576
# 524288
# 262144
# 131072
# 65536
# 32768
# 16384
# 8192
# 4096
# 2048
# 1024
# 512
# 256
# 128
# 64 <- наименьшее возможное кол-во адресов в этой сети