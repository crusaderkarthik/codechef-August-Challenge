x=int(input())
for i in range(x):
    y=list(map(int,input().split()))
    y1=y[0]+y[1]+y[2]
    y2=y[3]+y[4]+y[5]
    if y1<y2:
        print("2")
    else:
        print("1")
