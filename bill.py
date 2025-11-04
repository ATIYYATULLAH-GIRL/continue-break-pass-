billamount = float(input("Enter the total bill amount: "))
amountpaid = float(input("Enter the amount paid by the customer: "))
dueamount = billamount - amountpaid
if dueamount > 0:
    print("The customer still owes:", round(dueamount, 2))
elif dueamount < 0:
    print("The customer should receive a refund of:", round(abs(dueamount), 2))
else:
    print("The bill is fully paid. No due amount.")