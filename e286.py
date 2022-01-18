while 1:
    try:
        n=[]
        ans=[]
        sta=0
        for i in range(4):
            n.append(list(map(int,input().split())))
        for j in range(4):
            tmp=0
            for k in range(4):
                tmp=tmp+n[j][k]
            ans.append(tmp)
        print(ans[0],':',ans[1],sep="")
        print(ans[2],':',ans[3],sep="")
        if ans[0]>ans[1]:
            sta+=1
        elif ans[0]<ans[1]:
            sta+=-1
        if ans[2]>ans[3]:
            sta+=1
        elif ans[2]<ans[3]:
            sta+=-1
        if sta==0:
            print("Tie")
        elif sta==2:
            print("Win")
        else:
            print("Lose")
    except:
        break