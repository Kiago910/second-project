import random
number = random.randint(-10000, 10000)
i = number
char = str(i)
m=(len(char))
letter = m-1
last_digit=(char[letter])
if int(last_digit)>5:
    x=(f"last digit of {i} is")
    y=("{} and is greater than 5".format(last_digit))
    last=x+" "+y
    print(last)
if int(last_digit)==0:
     x=(f"last digit of {i} is")
     y=("{} and is zero".format(last_digit))
     z=x+" "+y
     print(z)
if int(last_digit)<6 and int(last_digit)!=0:
     x=(f"last digit of {i} is")
     y=("{} and is less than 6 and not 0".format(last_digit))
     less=x+" "+y
     print(less)