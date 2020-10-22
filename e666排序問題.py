while True:
    try:
      n1=input().split()
      n2=input()
      n3=input().split()
      list1=list(n2)
      list1.sort()
      for i in range(0,int(n1[1])):
        pos=int(n3[i])-1
        print(list1[pos],end="")
      print("\n")
    except:
        break
