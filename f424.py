while 1:
    try:
        n=int(input())-2
        ans=[1,3]
        for i in range(n):
            ans.append(ans[i]+ans[i+1])
        print(ans[n+1])
    except:
        break