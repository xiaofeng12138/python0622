
a=[3,5,2,8,4,7,9,1,0]

i = 0
while i < len(a) - 1:
    i += 1
    n = 0
    while n < len(a) - 1:
        if a[n] > a[n + 1]:
            a[n],a[ n + 1] = a[ n + 1 ],a[ n ]
        n += 1
    print(a)
