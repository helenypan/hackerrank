for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted
    a = int(input());A = set(input().split())
    b = int(input()); B = set(input().split())
    if a >b :
        print(False)
    else:
        print(len(A.difference(B)) == 0)