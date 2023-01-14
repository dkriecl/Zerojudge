while True:
    try:
        a,b=map(int,input().split())
        c=input()
        if c=="*":
            print(int(eval(a*b)))
        elif c=="/":
            print(int(eval(a/b)))
        elif c=="+":
            print(int(eval(a+b)))
        elif c=="-":
            print(int(eval(a-b)))
    except:
        break