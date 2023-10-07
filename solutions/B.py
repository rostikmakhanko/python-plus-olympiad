s = input().split()
a = [len(x) for x in s]
mx = max(a)
for w in s:
    if len(w) == mx:
        print(w)
        break
