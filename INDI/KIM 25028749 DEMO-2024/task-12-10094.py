ans = []
for n in range(4, 10000):
    st = '5' + n * '2'
    while '52' in st or '2222' in st or '1122' in st:
        st = st.replace('52', '11', 1)
        st = st.replace('2222', '5', 1)
        st = st.replace('1122', '25', 1)
    summ = sum(map(int, st))
    if summ == 64:
        ans.append(n)
print(max(ans))

# otvet: 156