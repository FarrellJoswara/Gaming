import random2
val1 = ""
if input("1 or 2 ") == "1": 
  while val1 != "quit":
      val1 = input("Enter value 1: ")
      print("value 1 is " + val1)
else:
  num = random2.randint(0,10)
  if input("pick a number between 0 and 10: " ) == str(num):
    print("congrats you got it")
  else: 
    print("so bad the number was " + str(num))




