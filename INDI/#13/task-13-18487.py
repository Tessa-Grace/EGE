from ipaddress import ip_network, ip_address

ans = []
for A in range(256):
    net = ip_network(f'116.242.{A}.26/255.255.255.224', False)
    for i in net:
        i = f'{int(i):032b}'
        if not(i[:16].count('1') >= i[16:].count('1')):
            break
    else:
        ans.append(A)

print(max(ans))