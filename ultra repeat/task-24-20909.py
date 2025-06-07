with open('24_20909.txt') as file:
    st = file.readline()

st = st.split('AB')
ans = 0
for i in range(len(st) - 100):
    ans = max(ans, len('AB'.join(st[i:i+101])))
print(ans + 2)