from ipaddress import ip_network, ip_address

net = ip_network('172.16.192.0/255.255.192.0')
cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 5 != 0:
        cnt += 1
print(cnt)

# otvet: 13003