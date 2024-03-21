f = open('26 (5).txt')
k = int(f.readline())
lst = [i.strip() for i in f.readlines()]
sp = []
for i in lst:
    i = i.split()
    sp.append([int(i[0]), int(i[0]) + int(i[1]), int(i[2])])
sp = sorted(sp, key=lambda x: x[0])

kas1 = []
kas2 = []
k1 = k2 = p = 0
x = 0
for i in range(0, 1000):
    sp = sp[x:]
    for t in sp:
        #print(t)
        if i == t[0]:
            if t[2] == 0:
                if len(kas1) == len(kas2) and len(kas1) < 15:
                    kas1 += [t]
                    k1 += 1
                elif len(kas1) > len(kas2) and len(kas2) < 15:
                    kas2 += [t]
                    k2 += 1
                elif len(kas1) < len(kas2) and len(kas1) < 15:
                    kas1 += [t]
                    k1 += 1
                else:
                    p += 1
            elif t[2] == 1:
                if len(kas1) < 15:
                    kas1 += [t]
                    k1 += 1

                else:
                    p += 1
            elif t[2] == 2:
                if len(kas2) < 15:
                    kas2 += [t]
                    k2 += 1
                else:
                    p += 1
            x = 1
            # print('Касса 1', len(kas1))
            # #print(k1)
            # print('Касса 2', len(kas2))
            # #print(k2)
            # print(p)

        else:
            x = 0


        #print('i ==', i)
        for t1 in kas1:
            if i == t1[1]:
                kas1.remove(t1)
        #print("касса 1", kas1)
        for t2 in kas2:
            if i == t2[1]:
                kas2.remove(t2)
        #print("касса 2", kas2)
        break


print(k2, p)

#
#
#
#
#





