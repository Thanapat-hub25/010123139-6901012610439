def encrypt(s, k):
    t = ""
    i = 0
    while i < len(s):
        c = s[i].upper()              # แปลงเป็นตัวพิมพ์ใหญ่
        if c.isalpha():               # เช็กว่าเป็นตัวอักษร
            code = ord(c) + k         # เลื่อนรหัส ASCII
            if code > ord("Z"):
                code = code - 26      # เกิน Z ให้วนกลับไป A
            t = t + chr(code)
        else:
            t = t + s[i]              # ไม่ใช่ตัวอักษร (เช่น ช่องว่าง) ใช้ตัวเดิม
        i = i + 1
    return t

def main():
    s = "Hello World"
    k = 3

    t = encrypt(s, k)
    print("Original :", s)
    print("Encrypted:", t)

    print()
    print("index\tchar\tASCII")
    table = ""
    i = 0
    while i < len(s):
        table = table + str(i) + "\t" + s[i] + "\t" + str(ord(s[i])) + "\n"
        i = i + 1
    print(table)

if __name__ == "__main__":
    main()