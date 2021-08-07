x = int(input())
for i in range(x):
    y = list(map(int, input().split()))
    a = set(y)
    if (len(a) == 4):
        print(2)
    elif (len(a) == 3):
        print(2)
    elif (len(a) == 2):
        y.sort()
        b = y[0]
        if(y.count(b) == 2):
            print(2)
        else:
            print(1)
    else:
        print(0)
