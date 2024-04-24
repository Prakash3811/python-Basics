def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

rows = int(input())
print_reverse_pyramid(rows)
