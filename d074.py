while 1:
    try:
        n=int(input())
        print(sorted(list(map(int,input().split())))[-1])
    except:
        break
