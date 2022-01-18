while 1:
    try:
        m=float(input())
        n=round(m*100)/100.0
        if len((str(n).split("."))[1])==2:
            print(n)
        elif 2-len((str(n).split("."))[1])!=0:
            print(str(n)[:str(n).find(".")+2],end="")
            for i in range(0,2-len((str(n).split("."))[1])):
                print("0",end="")
        else:
            print(n)
        print()
    except:
        break
