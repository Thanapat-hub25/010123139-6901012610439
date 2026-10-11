class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(self.name, self.score)

    def get_grade(self):
        if self.score >= 80:
            return "A"
        else:
            if self.score >= 70:
                return "B"
            else:
                if self.score >= 50:
                    return "C"
                else:
                    return "F"

def main():
    students = []
    students.append(Student("Somchai", 85))
    students.append(Student("Malee", 72))
    students.append(Student("Preecha", 45))

    i = 0
    while i < len(students):
        students[i].show()
        i = i + 1

    f = open("students.txt", "w")
    i = 0
    while i < len(students):
        s = students[i]
        f.write(s.name + "," + str(s.score) + "," + s.get_grade() + "\n")
        i = i + 1
    f.close()

    print()
    print("--- students.txt ---")
    with open("students.txt", "r") as file:
        for line in file:
            print(line, end="")

if __name__ == "__main__":
    main()