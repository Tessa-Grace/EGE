from ipaddress import ip_network

net = ip_network('218.194.82.148/255.255.255.192', False)

print(net[-2])

# otvet: 218.194.82.190
# otvet: 21819482190