while 1:
    try:
        n=list(map(str,input().split()))
        if n[1]=="+":
            print(int(n[0])+int(n[2]))
        elif n[1]=="-":
            print(int(n[0])-int(n[2]))
        elif n[1]=="*":
            print(int(n[0])*int(n[2]))
        elif n[1]=="/":
            print(int(n[0])//int(n[2]))
    except:
        break