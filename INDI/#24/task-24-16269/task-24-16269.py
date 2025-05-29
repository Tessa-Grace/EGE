with open('24_16269.txt') as f:
    st = f.readline()

for i in 'TUVW': st = st.replace(i, ' ')

for i in range(2):
    st = st.replace('XXX', 'XX XX')
    st = st.replace('YYY', 'YY YY')
    st = st.replace('ZZZ', 'ZZ ZZ')
m = st.split()
print(len(max(m, key=len)))
print(max(m, key=len))