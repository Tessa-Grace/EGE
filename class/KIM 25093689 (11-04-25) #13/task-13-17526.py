from ipaddress import ip_network

net = ip_network('172.16.128.0/255.255.192.0')

count = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 2 != 0:
        count += 1
print(count)

# otvet: 8192