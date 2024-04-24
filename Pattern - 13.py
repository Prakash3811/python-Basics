def print_continuous_right_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num*10, end=" ")
            num += 1
        print()

rows = int(input())
print_continuous_right_triangle(rows)
