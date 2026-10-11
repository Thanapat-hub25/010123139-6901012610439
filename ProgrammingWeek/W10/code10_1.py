class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    def show_info(self):
        print("Name:", self.name)
        print("BMI:", self.get_bmi())

    def get_bmi(self):
        return round(self.weight / (self.height * self.height), 2)

    def get_discount(self):
        return 0

    def get_price(self, price):
        return price - price * self.get_discount() / 100

class Student(Person):
    def __init__(self, name, weight, height, student_id):
        super().__init__(name, weight, height)
        self.student_id = student_id

    def show_info(self):
        super().show_info()
        print("Student ID:", self.student_id)

class Employee(Person):
    def __init__(self, name, weight, height, employee_id):
        super().__init__(name, weight, height)
        self.employee_id = employee_id

    def show_info(self):
        super().show_info()
        print("Employee ID:", self.employee_id)

    def get_discount(self):
        return 10

class Manager(Employee):
    def __init__(self, name, weight, height, employee_id, team_size):
        super().__init__(name, weight, height, employee_id)
        self.team_size = team_size

    def show_info(self):
        super().show_info()
        print("Team size:", self.team_size)

    def get_discount(self):
        return 20

def main():
    people = []
    people.append(Person("Anan", 60, 1.7))
    people.append(Student("Malee", 52, 1.6, "6601234"))
    people.append(Employee("Somchai", 75, 1.75, "E101"))
    people.append(Manager("Preecha", 82, 1.8, "M001", 8))

    i = 0
    while i < len(people):
        people[i].show_info()
        print("Price of 1000 =", people[i].get_price(1000))
        print()
        i = i + 1

if __name__ == "__main__":
    main()