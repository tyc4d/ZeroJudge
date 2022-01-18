c = int (input())
n = list(map(int,input().split()))
n1 = n
a = 0
b =[0,1,2,3]
for i in range (c):
   if n[i] // 10 > 0:
        n1[i] = n1[i] / 10
for i in range(c):
    for j in range (c-1):
        if n1[j] > n1[j+1]:
            n1[j] , n1[j+1] = n1[j+1] , n1[j]
            b[j] , b[j+1] = b[j+1] , b[j]
for i in range (c):
    print (int(n[b[i]]),end='')