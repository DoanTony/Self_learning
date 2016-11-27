import random
'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Extras:
- Randomly generate two lists to test this
'''
# ==== function practice =====
def sort_out_common_list(first_list,second_list):
    new_list= []
    for x in first_list:
        if (x in second_list) and (x not in new_list): # Avoid duplicate numbers in the new list
            new_list.append(x)
    return new_list
# ==============================
#=== variables =====
a = []
b = []
# ==================

for index in range(0,30):
    random_number = random.randrange(1, 100)
    a.append(random_number)
    random_number = random.randrange(1,100)
    b.append(random_number)

print("First array A : ",a) # Print A array with random numbers
print("Second array B : " , b) # Print B array with random numbers

common_list = sort_out_common_list( a , b )
print("Common numbers list between both array : " , common_list)