income=float(input("Enter your total income:"))
tax=float(input("Enter your tax level in %:"))
expenses=float(input("Enter the cost of your expenses:"))
currency=input("Enter your currency symbol:")

def availablemoney(income1,taxes1,expenses1,currency1):
    taxes1=taxes1/100
    remainingmoney1=round(income1-(income1*taxes1)-expenses1, 2)
    
    if remainingmoney1>0:
        return(f"{remainingmoney1}{currency1}")
    elif remainingmoney1==0:
        return("No money left")
    elif remainingmoney1<0:
        return("Insufficient funds")


print(availablemoney(income,tax,expenses,currency))