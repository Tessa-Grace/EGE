from ipaddress import ip_network

for mask in range(16, 25):
    net = ip_network(f'152.65.245.132/{mask}', False)
    for i in net:
        i = f'{int(i):032b}'
        if not(i[:16].count('0') >= i[16:].count('0')):
            break
    else:
        print(net.netmask)

# otvet:
# 255.255.252.0 <- otvet
# 255.255.254.0
# 255.255.255.0

# otvet: 252