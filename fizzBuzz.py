#this code simply shows how the fizz buzz game works this is asked in several python programming languages 

for num in range (1,101):
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
