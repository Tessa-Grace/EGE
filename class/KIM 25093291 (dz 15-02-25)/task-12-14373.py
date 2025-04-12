ans = []
for n in range(4, 1000):
    st = '3' + n * '5'
    while '333' in st or '555' in st:
        if '555' in st:
            st = st.replace('555', '35', 1)
        else:
            st = st.replace('333', '53', 1)
    ans.append(len(st))
print(max(ans))

# otvet: 17
