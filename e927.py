while 1:
    try:
        n=sorted(input())
        for i in range(len(n)):
            print(n[i],end="")
        print()
    except:
        break