while 1:
    try:
        n,m=list(map(int,input().split()))
        if m>n:
            ans=m-n
        elif m<n:
            ans=m-n+100
        elif m==n:
            ans=n
        print(ans)
    except:
        break