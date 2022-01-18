while 1:
    try:
        n=int(input())
        nums=[]
        for k in range(1,n+1):
            sum=0
            nums=[]
            for i in range(n):
                nums.append(int(input()))
            for j in range(1001):
                    if j*j>=nums[0] and j*j<=nums[1]:
                        sum+=j*j
            print("Case ",k,": ",sum,sep="")
    except:
        break