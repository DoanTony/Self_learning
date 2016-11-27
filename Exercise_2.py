#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
number = int(input("Enter a number :"))

#Check if input is a divider of 4
if number%4 == 0:
    print("This is a divider of 4")
elif number%2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")