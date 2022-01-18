while 1:
    try:
        n,w=list(map(int, input().split()))
        print(n//w)
    except:
        break