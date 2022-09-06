# creating our addition function
from unittest import result
def addition(a, b):
    return a + b 
# main program
def main():
    num1 = float(input(" enter your first number:\n"))
    num2 = float(input("enter your second number:\n"))
# calling our function
    result = addition(num1, num2)
    print("The result is:",result)
main()
