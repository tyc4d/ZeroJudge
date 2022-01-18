while 1==1:
    try:
        tgt=list(map(int,input().split()))
        n=int(input())
        for i in range(n):
            A=0
            B=0
            guess=list(map(int,input().split()))
            nonguess=sorted(set(guess))
            for j in range(len(nonguess)):
                if guess[j]==tgt[j]:
                    A+=1
                    continue
                for k in range(4):
                    if nonguess[j]==tgt[k]:
                        B+=1
                        break
            print(A,"A",B,"B",sep="")
            aa=input()
    except:
        break  