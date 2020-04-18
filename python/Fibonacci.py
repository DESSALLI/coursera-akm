#uses python3
n1 = 0
n2 = 1
count = int(input())
if count == 1 or count == 2:
    if count == 0:
        print(0)
    elif count == 1:
        print(1)
elif count > 1:
    i = 1
    while i < count:
        n3 = n1 + n2
        n4 = n3
        #print( i , "  ",n3)
        n1 = n2
        n2 = n3
        i = i + 1
print(n4)

