# Тимофей решил так

with open("24_21717.txt", "r") as f:
    f = f.read().split("RSQ")
    mn = 10**9
    for i in range(0, len(f) - 130):
        a = f[i : i + 131]
        a = "RSQ".join(a)
        if (
            not a[-1]
            or a[-1][-1] == "Q"
            and i + 132 < len(f)
            and f[i + 132]
            and f[i + 132][0][0] != "Q"
        ):
            a += "_"
        mn = min(mn, len(a))
print(mn)
