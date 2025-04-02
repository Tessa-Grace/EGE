def is_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

ans = []
for n in range(4, 1000):
    st = '>' + 25 * '0' + n * '1' + 25 * '2'
    while '>1' in st or '>2' in st or '>0' in st:
        st = st.replace('>1', '22>')
        st = st.replace('>2', '2>')
        st = st.replace('>0', '1>')
    st = st.replace('>', '')
    summ = sum(map(int, st))
    if is_prime(summ):
        ans.append(n)
print(min(ans))

# otvet: 7

