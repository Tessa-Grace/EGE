from ipaddress import ip_network

net = ip_network('192.168.32.160/255.255.255.240')

count = 0
for i in net:
    ip = f'{int(i):032b}'
    if ip.count('0') > 21:
        count += 1
print(count)

# otvet: 11