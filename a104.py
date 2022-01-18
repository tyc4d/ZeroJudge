while 1:
    try:
        n=int(input())
        m=list(map(int, input().split()))
        m=sorted(m)
        for i in range(n):
            print(m[i],end=" ")
        print()
    except:
        break