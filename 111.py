s = input()
for i in range(len(s)):
    if i != len(s) - 1:
        print(ord(s[i]), ', ', sep='', end='')
    else:
        print(ord(s[i]))