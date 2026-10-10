def sum_even(n):
    total = 0
    count = 2
    while count <= n:
        total = total + count
        count = count + 2      
    return total

def sum_odd(n):
    total = 0
    count = 1
    while count <= n:
        total = total + count
        count = count + 2      
    return total

def main():
    n = 5
    print("Even sum up to", n, "=", sum_even(n))
    print("Odd sum up to", n, "=", sum_odd(n))
    n = 10
    print("Even sum up to", n, "=", sum_even(n))
    print("Odd sum up to", n, "=", sum_odd(n))
