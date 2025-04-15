# ___________________________________
#             1 METHOD
#____________________________________
from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'223.167.{A}.167/26', False) # можно маску 255.255.255.192 задать как кол-во единиц, а False, если возникает ошибка с 'has host bit set'
    cnt = 0
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('0') <= i[16:].count('0'):
            cnt += 1
    if cnt == len(list(net)):
        print(A)
# ___________________________________
#             2 METHOD (better)
#____________________________________
from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'223.167.{A}.167/26', False)
    for i in net:
        i = f'{int(i):032b}'
        if not (i[:16].count('0') <= i[16:].count('0')):
            break
    else:
        print(A)

# otvet: 248