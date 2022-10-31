i = 0
while i < 100:
    i = i + 1
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    if i%3 == 0:
       print("Fizz")
       continue
    if i%5 == 0:
        print ("Buzz")
        continue
    print(i)
