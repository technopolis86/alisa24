s, p = [], []
n, m = map(int, input().split())
for i in range(n):
    t = input().split()
    s += [t]
input()
for i in range(n):
    t = input().split()
    p += [t]
r = set()
for i in range(n):
    for j in range(m):
        if s[i][j] != '.' and (s[i][j] != p[i][j]):
            r.add(s[i][j])
if r:
    print(len(r))
    for i in sorted(r):
        print(i)
else:
    print(11111222222)







