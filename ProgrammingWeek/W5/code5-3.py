a = [72, 85, 40, 91, 66]

total = 0
highest = a[0]
best_index = 0
passed = 0

i = 0
while i < len(a):
    print("a[", i, "] =", a[i])     # พิมพ์ index และสมาชิก

    total = total + a[i]            # หาผลรวม

    if a[i] > highest:              # หาค่าสูงสุด
        highest = a[i]
        best_index = i

    if a[i] >= 50:                  # นับคนสอบผ่าน
        passed = passed + 1

    i = i + 1

average = total / len(a)

print("Sum =", total)
print("Average =", average)
print("Highest =", highest, "at index", best_index)
print("Passed =", passed, "out of", len(a))