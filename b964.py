n=int(input())
nums=sorted(list(map(int,input().split())))
for i in range(n):
    print(nums[i],end=" ")
print()
for k in range(n-1,-1,-1):
    if nums[k]<60:
        print(nums[k])
        if k==n-1:
            print("worst case")
        break
for j in range(n):
    if nums[j]>60:
        if j==0:
            print("best case")
        print(nums[j])
        break
