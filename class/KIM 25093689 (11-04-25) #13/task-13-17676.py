from ipaddress import ip_network

net = ip_network('115.192.0.0/255.192.0.0')

count = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 3 != 0:
        count += 1
print(count)

# otvet: 2796202