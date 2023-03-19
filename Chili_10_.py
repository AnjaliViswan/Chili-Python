a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
for i in c:
    counter = 0
    for x in c:
        if i == x:
            counter+=1
            if counter == 2:
                c.remove(i)

print(c)