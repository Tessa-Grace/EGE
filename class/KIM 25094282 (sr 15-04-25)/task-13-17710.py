from ipaddress import ip_network

net = ip_network(f'214.187.224.0/255.255.224.0')

count = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 6 != 0 and i[-4:] == '1000':
        count += 1
print(count)

# otvet: 427