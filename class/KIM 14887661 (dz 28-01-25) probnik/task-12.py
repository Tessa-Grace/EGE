ans = []
for n in range(2, 1000):
    st = '>' + 21 * '0' + n * '1' + 11 * '2'
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>', 1)
        st = st.replace('>2', '2>', 1)
        st = st.replace('>0', '1>', 1)
    st = st.replace('>', '')
    summ = sum(map(int, st))
    if summ % n == 0:
        ans.append(n)
print(min(ans))

# otvet: 43