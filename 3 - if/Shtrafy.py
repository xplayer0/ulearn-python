l, r, v = int(input()), int(input()), int(input())

if l <= v <= r:
  print(500)
elif v > r:
  print(10000)
else:
  print(0)