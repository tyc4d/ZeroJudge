while 1:
    try:
        num=list(map(int,input().split()))
        ass=num[0]/num[1]
        n=num[2]+1
        if n-len((str(ass).split("."))[1])!=0:
            print(str(ass)[:str(ass).find(".")+n],end="")
            for i in range(1,n-len((str(ass).split("."))[1])):
                print("0",end="")
        else:
            print(str(ass)[:str(ass).find(".")+n])
        print()
    except:
        break