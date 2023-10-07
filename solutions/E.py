n = int(input())
a = [int(x) for x in input().split()]
a.sort()
v = []
p = []
for i in range(1, n):
    b = [int(x) for x in input().split()]
    b.sort()
    n1 = len(b)
    f = None
    for j in range(n1):
        if b[j] != a[j]:
            f = a[j]
            break
    if f == None:
        f = a[n1]
    if i%2==1:
        v.append(f)
    else:
        p.append(f)
    a = b.copy()
if n%2==1:
    v.append(a[0])
else:
    p.append(a[0])
v.sort()
p.sort()
for x in v:
    print(x, end=' ')
print('')
for x in p:
    print(x, end=' ')
