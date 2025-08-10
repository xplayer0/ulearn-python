n, x, y = int(input()), int(input()), int(input())
# (x,y)=(1,1) -> black

if ((x % 2 == 1) and (y % 2 == 0)) or ((x % 2 == 0) and (y % 2 == 1)):
  print("white")
else:
  print("black")