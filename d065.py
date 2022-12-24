while True:
    try:
        a,b,c=map(int,(input()).split(','))
        print(max(a,b,c))
    except:
        break