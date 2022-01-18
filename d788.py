n=int(input())
soc=[]
for i in range(n):
    tmp=int(input())
    soc.append(tmp)
    soc=sorted(soc)
    for j in range(len(soc)):
        if tmp<soc[i]:
