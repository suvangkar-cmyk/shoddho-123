cost=float(input(" please enter the Actual product price:"))
amount=float(input(" please enter the sales Amount:"))
if (amount > cost):
    amount= amount - cost
    print("Total profit = {0}".format(amount))
else:
    print("No Profit!!!")