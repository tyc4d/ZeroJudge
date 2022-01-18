while 1:
    try:
        f13=['1m', '1p', '1s', '1z', '2z', '3z', '4z', '5z', '6z', '7z', '9m', '9p', '9s']
        same=0
        num=sorted(input().split())
        unique = []
        for name in num:
            if name not in unique:
                unique.append(name)
        if num==f13:
            print('13')
        else:
            for i in range(13):
                for j in range(len(unique)):
                    if unique[j]==f13[i]:
                        same=same+1
            if same==12:
                print("1")
            else:
                print(same)
    except:
        break