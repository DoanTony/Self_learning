#Odd and Even numbers
number = int(input("Enter a number :"))

#Check if input is a divider of 4
if number%4 == 0:
    print("This is a divider of 4")
elif number%2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")