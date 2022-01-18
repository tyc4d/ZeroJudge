while 1:
    try:
        n,m=list(map(int,input().split()))
        feed=[]
        fRange=[]
        for f in range(n):
            feed.append(list(map(int,input().split())))
        for k in range(m):
            x1,y1,x2,y2=list(map(int,input().split()))
            ans=0
            for i in range(abs(x2-x1)+1):
                for j in range(abs(y2-y1)+1):
                    ans+=feed[i][j]
            print(ans)
    except:
        break