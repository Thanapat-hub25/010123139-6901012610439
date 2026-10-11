import os

def main():
    f = open("sample.txt", "w")
    f.write("Hello, everybody\n")
    f.close()

    print("Current directory:", os.getcwd())
    print()

    names = os.listdir()
    i = 0
    while i < len(names):
        name = names[i]
        if os.path.isfile(name):
            print(name, "(file,", os.path.getsize(name), "bytes)")
        else:
            if os.path.isdir(name):
                print(name, "(folder)")
        i = i + 1

    print()
    if os.path.exists("sample.txt"):
        print("sample.txt exists")
    else:
        print("sample.txt not found")

    if os.path.exists("missing.txt"):
        print("missing.txt exists")
    else:
        print("missing.txt not found")

if __name__ == "__main__":
    main()