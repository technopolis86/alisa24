a = int(input())
b = int(input())
n = int(input())
k = b * n
r = a * n + k // 100
k %= 100
print(r, k)