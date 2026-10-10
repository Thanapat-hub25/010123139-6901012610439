def print_diamond(h):
     i = 1
     while i <= h:
          space = h - i
          star = (2 * i) -1

          s = 0
          while s < space:
               print(" ", end="")
               s += 1
          t = 0
          while t < star:
               print("*",end="")
               t += 1
          print()
          i += 1

     i = h - 1
     while i >= 1:
          spaces = h - i
          stars = 2 * i - 1

          s = 0
          while s < spaces:
               print(" ", end="")
               s = s + 1

          t = 0
          while t < stars:
               print("*", end="")
               t = t + 1

          print()
          i = i - 1
print_diamond(5)
