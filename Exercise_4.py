#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

while True: #loop while user didn't enter a valid number
    try:
        user_number_input = int(input("Enter a number: "))
        list_divisors = []

        for index in range(1,user_number_input +1): #+1 to include the input number
            if user_number_input%index == 0:
                list_divisors.append(index)

        print(list_divisors)
        break
    except ValueError:
        print("Please enter a valid number")