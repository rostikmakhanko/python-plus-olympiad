s = input()
e = True
for c in s:
    if c != s[0]:
        e = False
u = True
for i in range(1, 4):
    if int(s[i]) - 1 != int(s[i-1]):
        u = False
if not e and not u:
    print('No')
else:
    print('Yes')
