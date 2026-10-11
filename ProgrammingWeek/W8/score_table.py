def print_2D(m):
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            print(m[i][j], end="\t")
            j = j + 1
        print()
        i = i + 1

def sum_row(m, r):
    total = 0
    j = 0
    while j < len(m[r]):
        total = total + m[r][j]
        j = j + 1
    return total

def count_at_least(m, limit):
    count = 0
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] >= limit:
                count = count + 1
            j = j + 1
        i = i + 1
    return count

def add_matrix(A, B):
    result = []
    i = 0
    while i < len(A):
        row = []
        j = 0
        while j < len(A[i]):
            row.append(A[i][j] + B[i][j])
            j = j + 1
        result.append(row)
        i = i + 1
    return result

def main():
    midterm = [[20, 35, 28],
               [45, 15, 30],
               [38, 42, 25]]
    final = [[30, 40, 22],
             [40, 28, 35],
             [25, 45, 41]]

    print("Midterm (rows = students, columns = subjects)")
    print_2D(midterm)

    print()
    print("Final")
    print_2D(final)

    total = add_matrix(midterm, final)
    print()
    print("Total = Midterm + Final")
    print_2D(total)

    print()
    i = 0
    while i < len(total):
        print("Student", i + 1, "sum =", sum_row(total, i))
        i = i + 1

    print()
    print("Subjects with total >= 60:", count_at_least(total, 60))

if __name__ == "__main__":
    main()