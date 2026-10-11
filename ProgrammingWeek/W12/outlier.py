import math

def get_mean(a):
    total = 0
    i = 0
    while i < len(a):
        total = total + a[i]
        i = i + 1
    return total / len(a)

def get_std(a):
    mean = get_mean(a)
    total = 0
    i = 0
    while i < len(a):
        diff = a[i] - mean
        total = total + diff * diff
        i = i + 1
    return math.sqrt(total / len(a))

def find_outliers(a, k):
    mean = get_mean(a)
    std = get_std(a)
    result = []
    i = 0
    while i < len(a):
        if abs(a[i] - mean) > k * std:
            result.append(i)
        i = i + 1
    return result

def remove_indexes(a, indexes):
    result = []
    i = 0
    while i < len(a):
        found = False
        j = 0
        while j < len(indexes):
            if indexes[j] == i:
                found = True
            j = j + 1
        if not found:
            result.append(a[i])
        i = i + 1
    return result

def main():
    data = [50, 52, 48, 51, 49, 50, 95, 47]

    print("Data:", data)
    print("Mean:", round(get_mean(data), 2))
    print("Std :", round(get_std(data), 2))

    outliers = find_outliers(data, 2)
    print()
    if len(outliers) == 0:
        print("No outlier found")
    else:
        print("Outliers (more than 2 std from mean):")
        i = 0
        while i < len(outliers):
            print("  index", outliers[i], "value", data[outliers[i]])
            i = i + 1

        cleaned = remove_indexes(data, outliers)
        print()
        print("Data without outliers:", cleaned)
        print("Mean without outliers:", round(get_mean(cleaned), 2))

if __name__ == "__main__":
    main()