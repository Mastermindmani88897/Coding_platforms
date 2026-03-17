def utility(a, b, opr):
    #code here
    if opr==1:
        a=a+b
        a=str(a)
        print(a,end="")
    elif opr==2:
        a=a-b
        a=str(a)
        print(a,end="")
    elif opr==3:
        a=a*b
        a=str(a)
        print(a,end="")
    else:
        print("Invalid Input",end="")