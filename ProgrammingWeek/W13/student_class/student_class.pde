class Student {
  String name;
  int score;

  Student(String name, int score) {
    this.name = name;
    this.score = score;
  }

  String getGrade() {
    if (score >= 80) {
      return "A";
    } else if (score >= 70) {
      return "B";
    } else if (score >= 50) {
      return "C";
    } else {
      return "F";
    }
  }

  void show() {
    println(name + " " + score + " " + getGrade());
  }
}

void setup() {
  Student[] students = new Student[3];
  students[0] = new Student("Somchai", 85);
  students[1] = new Student("Malee", 72);
  students[2] = new Student("Preecha", 45);

  for (int i = 0; i < students.length; i = i + 1) {
    students[i].show();
  }
}
