def read_numbers(filename):
    a = []
    with open(filename, "r") as file:
        for line in file:
            num = int(line)
            a.append(num)
    return a

def main():
    with open("scores.txt", "w") as file:
        file.write("72\n")
        file.write("85\n")
        file.write("40\n")
        file.write("91\n")
        file.write("66\n")

    try:
        a = read_numbers("scores.txt")
    except FileNotFoundError:
        print("Error: scores.txt is not found")
        return

    print("Scores =", a)

    total = 0
    highest = a[0]
    lowest = a[0]
    i = 0
    while i < len(a):
        total = total + a[i]
        if a[i] > highest:
            highest = a[i]
        if a[i] < lowest:
            lowest = a[i]
        i = i + 1
    average = total / len(a)

    with open("summary.txt", "w") as file:
        file.write("Sum = " + str(total) + "\n")
        file.write("Average = " + str(average) + "\n")

    with open("summary.txt", "a") as file:
        file.write("Highest = " + str(highest) + "\n")
        file.write("Lowest = " + str(lowest) + "\n")

    print()
    print("--- summary.txt ---")
    with open("summary.txt", "r") as file:
        for line in file:
            print(line, end="")

    print()
    try:
        b = read_numbers("not_exist.txt")
    except FileNotFoundError:
        print("Error: not_exist.txt is not found")

if __name__ == "__main__":
    main()