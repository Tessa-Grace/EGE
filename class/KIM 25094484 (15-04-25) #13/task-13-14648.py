from ipaddress import ip_network, ip_address

net_ip = ip_address('218.48.192.0')
cnt = 0
for mask in range(16, 25):
    net = ip_network(f'218.48.192.56/{mask}', False)
    if net.num_addresses >= 502 and net_ip == net.network_address: # более 502, а не 500, так есть общий и широковещательнй адрес
        cnt += 1
print(cnt)

# otvet: 6
