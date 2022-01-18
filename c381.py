while 1:
    try:
        n=list(map(int,input().split()))
        m=''
        for i in range(0,n[0]):
            m=m+input()
        ns=list(map(int,input().split()))
        for j in range(0,n[1]):
            print(m[ns[j]-1],end="")
        print()
    except:
        break