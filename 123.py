x = int(input())
while x % 21 != 0:
    if x % 3 == 0:
        print("несчастливое")
    elif x % 7 == 0:
        print("опасное")
    else:
        print(x)
    x = int(input())
if x % 21 == 0:
    print('Караул!')