for num in range(1, 101):       
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" )
    elif num % 5 == 0:
        print("Buzz", end=" ")
    elif num !=0:
        print(num, end=" ")
# % gives the remeinder of the number being divided