lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 3]]
x = 3
for i in lst:
    print(i)
    if x == i[2]:
        lst.remove(i)
print(lst)