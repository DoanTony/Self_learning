#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

# == Functions ====

def isPalindrome(user_string_input):
    lower_case_string = user_string_input.lower() # lowercase the string for check case sensitivity
    reverse_string =   lower_case_string[::-1] #[begin:end:step]
    if  lower_case_string == reverse_string:
        return  user_string_input + " is a palindrome"
    else:
        return  user_string_input + " is not a palindrome"

# ==============================

print(isPalindrome(input("Enter a word : ")))
