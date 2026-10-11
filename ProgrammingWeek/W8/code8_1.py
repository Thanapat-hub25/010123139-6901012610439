def show(a):
    i = 0
    while i < len(a):
        print(a[i], end=" ")
        i = i + 1
    print()

def add_bonus_all(a, x):
    i = 0
    while i < len(a):
        a[i] = a[i] + x
        i = i + 1

def add_bonus_one(a, x):
    a = a + x

def main():
    scores = [60, 75, 82]
    print("Before          :", end=" ")
    show(scores)

    add_bonus_all(scores, 5)
    print("add_bonus_all   :", end=" ")
    show(scores)

    score = 60
    add_bonus_one(score, 5)
    print("add_bonus_one   :", score)

if __name__ == "__main__":
    main()