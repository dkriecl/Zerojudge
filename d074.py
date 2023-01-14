while True:
    try:
        n=int(input())
        print(max(list(map(int,input().split()))))
    except:
        break