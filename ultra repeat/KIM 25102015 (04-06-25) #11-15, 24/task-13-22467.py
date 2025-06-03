from ipaddress import *

count = 0
for mask in range(33):
    net = ip_network(f"192.214.116.184/{mask}", False)
    if bin(int(net.network_address))[2:].count("1") % 5 == 0 and ip_address(
        "192.214.116.184"
    ) not in [net.network_address, net.broadcast_address]:
        count += 1
print(count)

# otvet: 5