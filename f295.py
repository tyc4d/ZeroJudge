while 1:
    try:
        n = int(input())
        m = []
        pos = []

        for i in range(n):
            m.append(input())

        for j in range(n):
            pos.append(list(map(int,input().split())))

        ans_array = []

        for k in range(n):
            pos1 = pos[k][0]-1
            pos2 = pos[k][1]-1
            ans = m[k][:pos1] + m[k][pos2] + m[k][pos1+1:]
            ans = ans[:pos2] + m[k][pos1] + ans[pos2+1:]
            ans_array.append(ans)

        for b in range(len(ans_array)-1):
            print(ans_array[b],end=" ")
        print(ans_array[b+1],end=".")
        print()
    except:
        break