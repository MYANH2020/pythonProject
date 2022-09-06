# Get the loan details
from calendar import month


money_owed=float(input(" how much money do you owe, in dollars\n")) #$50,000
ap_rate = float(input(" what is the annual percentage rate?\n")) # 3%
payment = float(input("what will your monthly payment be, in dollars?\n"))#$1,000
months = int(input("how many months do you want to see results for?\n"))#24
#divide ap_rate by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = ap_rate/100/12
for i in range(months):
    # add in interest
    interest_paid = money_owed*monthly_rate
    money_owed = money_owed+interest_paid
    if (money_owed- payment<0):
        print("The last payment is", money_owed)
        print(" you pay off the loan in", i+1, "months")
        break
    #make payment
    money_owed = money_owed - payment
    #print the result after this month
    print("Paid", payment, " of which", interest_paid, " was interest.", end='')
    print(" now I owed", money_owed)
    