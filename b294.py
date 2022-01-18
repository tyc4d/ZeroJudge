while 1:
    try:
        n=int(input())
        m=input().split()
        sum=0
        for i in range(n):
            sum=sum+int(m[i])*(i+1)
        print(sum)
    except:
        break