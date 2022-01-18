while 1:
    try:
        nums=sorted(list(map(int,input().split())))
        last=nums[0]
        seen=0
        for i in range(len(nums)):
            #print("checkto",nums[i],"seen",seen,"last",last)
            if nums[i]==last:
                seen+=1
            else:
                if seen<2:
                    print(nums[i-1])
                    break
                else:
                    last=nums[i]
                    seen=0
    except:
        break