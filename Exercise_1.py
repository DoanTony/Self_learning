#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
import sys
import datetime

#Get current year
date = datetime.datetime.now()
year_now = date.year

name = input("Enter your full name : ")
age = int(input("Enter your age : "))

#EXTRA: number of times to print the result
while True:
    number = int(input("Enter a number between 1-10 : "))
    if(number>0) and (number<=10):
        break


#print while calculating in what year they will be age 100
for i in range(0,number):
    print("{} will be 100 in {}".format(name,(year_now + (100- age))))


