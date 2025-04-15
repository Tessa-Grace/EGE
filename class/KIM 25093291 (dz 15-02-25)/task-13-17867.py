from ipaddress import ip_network

net = ip_network(f'172.16.168.0/255.255.248.0')

count = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 5 == 0:
        count += 1
print(count)

# otvet: 385