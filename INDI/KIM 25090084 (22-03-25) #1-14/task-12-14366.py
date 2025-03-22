ans = []

for n in range(4, 10000):
    st = '9' + n * '6'
    while '96' in st or '6666' in st or '1166' in st:
        st = st.replace('96', '11')
        st = st.replace('6666', '9')
        st = st.replace('1166', '69')
        if sum(map(int, st)) % 37 == 0:
            ans.append(n)
print(min(ans))

# otvet: 19