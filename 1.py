val = 0
top = [0, 0, 0]
ls = []
for i in range(2251):
    x = input()
    if x == "":
        s = sum(ls)
        top.sort()
        top.reverse()
        if s > top[2]:
            top[2] = s
        elif s > top[1]:
            top[1] = s
        elif s > top[0]:
            top[0] = s
        ls = []
    else:
        ls.append(int(x))

print(sum(top))
