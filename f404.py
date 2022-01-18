while 1:
    try:
        n=int(input())
        count=0
        hole=['a','b','d','e','o','p','q','g']
        for i in range(n):
            num=list(map(int,input().split()))
            m=list(input())
            d=ord(m[num[0]-1])-96
            for j in range(1,27-d):
                poss=chr(ord(m[num[0]-1])+j)
                count=0
                for k in range(0,8):
                    if poss==hole[k]:
                        break
                    elif poss!=hole[k]:
                        count=count+1
                if count==8:
                    m.pop()
                    m.append(poss)
                    break
            for h in range(len(m)):
                print(m[h],end="")
    except:
        break
