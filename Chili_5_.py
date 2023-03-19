a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if a>b:
    for i in a:
        if i not in b:
            a.remove(i)
    print(a)
else:
    for i in b:
        if i not in a:
            b.remove(i)
    print(b)

