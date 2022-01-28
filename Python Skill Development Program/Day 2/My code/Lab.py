# simple interest calculator

def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si


# Driver code
simple_interest(8, 6, 8)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# check number is positive negative or zero

num = float(input("Input a number: "))
if num > 0:
   print("It is positive number")
elif num == 0:
   print("It is Zero")
else:
   print("It is a negative number")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Factorial number generator

# user input
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       factorial = factorial*i
   print("The factorial of", num, "is", factorial)

# week day using user input

weekday = int(input("Enter weekday day number (1-7) : "))

if weekday == 1:
    print("\nMonday")

elif weekday == 2:
    print("\nTuesday")

elif(weekday == 3):
    print("\nWednesday")

elif(weekday == 4):
    print("\nThursday")

elif(weekday == 5):
    print("\nFriday")

elif(weekday == 6):
    print("\nSaturday")

elif (weekday == 7):
    print("\nSunday")

else:
    print("\nPlease enter weekday number between 1-7.")
   

