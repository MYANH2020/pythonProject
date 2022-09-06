# display variable
from curses import A_UNDERLINE


amount = 1000
tax = .07
# Data type conversion function
# float to int
total = int(amount + amount*tax)
# print out
print(total)
# int to float
total = float(amount + amount*tax)
print(total)
#text, string, single or double quote is ok.
name ='hello'
print(name)
# cause errors
#name1 = 'Sarah's store '
# correct 
name3 = "Sarah's store "
print(name3)
hello = " hello"
name =  input("What is your name?")
greeting = hello + " "+ name
print(greeting)
#my_name = input(" what is your name?")
#print(" the customer's name is:")
#print(my_name)
age = int(input("how old are you?"))
# whole number division or integer division
decades= age//10
years = age %10
print(" you are "+ str(decades)+" decades old\n"+"and"+ str(years)+"years old")
