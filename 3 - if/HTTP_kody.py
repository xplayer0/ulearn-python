x = int(input())

if x == 200:
  print("OK")
elif 200 < x < 300:
    print("Success")
elif x == 404:
    print("Not Found")
elif 500 <= x < 600 and x != 501:
    print("Server error")
elif x == 501:
    print("Not implemented")
else:
  print("501")