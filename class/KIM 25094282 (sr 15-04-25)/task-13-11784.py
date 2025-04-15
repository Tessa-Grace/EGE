from ipaddress import ip_network

for A in range(255):
    net = ip_network(f'248.112.{A}.35/255.255.255.240', False)
    for i in net:
        i = f'{int(i):032b}'
        if not(i[:16].count('0') <= i[16:].count('0')):
            break
    else:
        print(A)

# otvet: 224