# 17675

st = '9' * 134

while '22222' in st or '9999' in st:
    if '22222' in st:
        st = st.replace('22222', '99', 1)
    else:
        st = st.replace('9999', '2', 1)
print(st)

# otvet: 22


