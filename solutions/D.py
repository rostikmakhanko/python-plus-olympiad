answer = []
def go(a, i, v, p, ans):
    n = len(a)
    if i >= n:
        global answer
        answer = ans
        return
    if a[i] <= v:
        ans1 = ans + ['v']
        go(a, i+1, v-a[i], p, ans1)
    if a[i] <= p:
        ans1 = ans + ['p']
        go(a, i+1, v, p-a[i], ans1)

a = [int(x) for x in input().split()]
v, p = input().split()
v = int(v)
p = int(p)
s = sum(a)
if v >= s and p >= s:
    print("They both can do it!")
elif v >= s:
    print("Vasyl can do it!")
elif p >= s:
    print("Petro can do it!")
elif v + p < s:
    print("They can not do it!")
else:
    go(a, 0, v, p, [])
    if len(answer) > 0:
        v1 = []
        p1 = []
        i = 1
        for x in answer:
            if x == 'v':
                v1.append(i)
            else:
                p1.append(i)
            i += 1
        print("They need to work together!")
        vs = "Vasyl: "
        for x in v1:
            vs += str(x) + " "
        ps = "Petro: "
        for x in p1:
            ps += str(x) + " "
        print(vs)
        print(ps)
    else:
        print("They can not do it!")
