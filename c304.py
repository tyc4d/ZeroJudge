while 1:
    try:
        n=list(map(int,input()))
        ans=n[::-1]
        for i in range(len(n)):
            ans[i]=ans[i]+n[i]
        for j in range(len(ans)):
            print(ans[j],end="")
        print()
    except:
        break
