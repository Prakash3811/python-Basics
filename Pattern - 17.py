def print_pattern(n):
    for i in range(n, 0, -1):
        print("  " * (n - i), end="")
        for j in range(0, i):
            print(chr(65 + j), end=" ")
        print()


n=int(input())
print_pattern(n)
