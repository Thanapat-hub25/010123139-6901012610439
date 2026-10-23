void setup() {
  int[] scores = { 72, 85, 40, 91, 66 };

  int i = 0;
  while (i < scores.length) {
    println("scores[" + i + "] = " + scores[i]);
    i = i + 1;
  }

  int total = 0;
  for (int j = 0; j < scores.length; j = j + 1) {
    total = total + scores[j];
  }
  float average = (float) total / scores.length;

  int highest = scores[0];
  for (int x : scores) {
    if (x > highest) {
      highest = x;
    }
  }

  int[] count = new int[4];
  for (int x : scores) {
    if (x >= 80) {
      count[0] = count[0] + 1;
    } else if (x >= 70) {
      count[1] = count[1] + 1;
    } else if (x >= 50) {
      count[2] = count[2] + 1;
    } else {
      count[3] = count[3] + 1;
    }
  }

  println();
  println("Sum = " + total);
  println("Average = " + average);
  println("Highest = " + highest);
  println("A = " + count[0] + ", B = " + count[1] + ", C = " + count[2] + ", F = " + count[3]);
}
