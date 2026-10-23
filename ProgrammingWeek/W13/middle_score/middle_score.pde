float cal_middle(int x1, int x2) {
  return (x1 + x2) / 2.0;
}

int cal_middle_int(int x1, int x2) {
  return (x1 + x2) / 2;
}

void setup() {
  println(5 / 2);
  println(5 / 2.0);
  println();

  println("Middle of 70 and 85 (int)  : " + cal_middle_int(70, 85));
  println("Middle of 70 and 85 (float): " + cal_middle(70, 85));
}
