from os import sep
#expenses =[10.50, 6, 8, 4, 7]
#sum = 0
#for x in expenses:
    #sum = sum + x
#print("You spent $", sum," on lunch this week", sep=(''))
#expenses2 = range(7)
#print(expenses2)
total = 0
expenses3 = []
num_expenses = int(input(" enter number of expenses:\n"))
for i in range(num_expenses):
    expenses3.append(float(input("enter an expense\n")))
    total = sum(expenses3)
    print("you spend $", total, sep='')