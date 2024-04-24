def print_pattern(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            row = ' '.join(str(n) for n in range(i, 0, -1))
        else:
            row = ' '.join(str(n) for n in range(1, i + 1))
        print(row)

n = int(input())
print_pattern(n)
