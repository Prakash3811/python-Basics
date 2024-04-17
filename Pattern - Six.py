n=int(input())

spaces = n-1
stars = 1

for i in range(n):
    for j in range(spaces):
        print(" ",end ="")
    
    for j in range(stars):
        print("*",end = "")
    print()
    
    spaces = spaces - 1
    stars = stars + 1
