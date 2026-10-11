import matplotlib.pyplot as plt

def read_numbers(filename):
    a = []
    with open(filename, "r") as file:
        for line in file:
            a.append(int(line))
    return a

def main():
    f = open("scores.txt", "w")
    f.write("72\n85\n40\n91\n66\n58\n77\n55\n")
    f.close()

    scores = read_numbers("scores.txt")

    quiz = []
    i = 0
    while i < len(scores):
        quiz.append(i + 1)
        i = i + 1

    plt.plot(quiz, scores, linestyle='--', marker='o')
    plt.title("Scores of Each Quiz")
    plt.xlabel("Quiz")
    plt.ylabel("Score")
    plt.show()

    a_count = 0
    b_count = 0
    c_count = 0
    f_count = 0
    i = 0
    while i < len(scores):
        if scores[i] >= 80:
            a_count = a_count + 1
        elif scores[i] >= 70:
            b_count = b_count + 1
        elif scores[i] >= 50:
            c_count = c_count + 1
        else:
            f_count = f_count + 1
        i = i + 1

    grades = ['A', 'B', 'C', 'F']
    counts = [a_count, b_count, c_count, f_count]

    plt.bar(grades, counts, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title("Number of Scores in Each Grade")
    plt.ylabel("Count")
    plt.show()

    plt.pie(counts, labels=grades)
    plt.title("Grade Proportion")
    plt.show()

if __name__ == "__main__":
    main()