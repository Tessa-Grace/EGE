from ipaddress import ip_network

count = 0
for A in range(256):
    net = ip_network(f'207.0.{A}.167/255.255.255.192', False)

    for i in net:
        i = f'{int(i):032b}'
        if not(i[:16].count('0') > i[16:].count('0')):
            break
    else:
        count += 1

print(count)

# otvet: 37