def sum_m_to_n(a, m, n):
    total = 0
    i = m
    while i <= n:
        total = total + a[i]
        i = i + 1
    return total

def is_sorted(a):
    ok = True                          
    i = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            ok = False                
        i = i + 1
    return ok

def main():
    a = [3, 8, 12, 15, 20]
    b = [5, 9, 2, 14, 7]

    print("a =", a)
    print("Sum index 1 to 3 =", sum_m_to_n(a, 1, 3))
    print("a sorted?", is_sorted(a))

    print()
    print("b =", b)
    print("Sum index 0 to 4 =", sum_m_to_n(b, 0, 4))
    print("b sorted?", is_sorted(b))

if __name__ == "__main__":
    main()