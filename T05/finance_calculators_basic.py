import math
# Financial intrest calculator with 2 types of investments, chosen by the user at the beginning of the process

# I - Investment/Bond choice Menu

print("Welcome to the Financial Calculator! Please type in the phrases from the list below:")
print("\n \t investment" + " - " "to calculate the amount of intrest you'll earn on you investment")
print("\n \t bond" + "\t    - " "to calculate the amount you'll have to pay on a home loan")
phrase = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# II - Calculator - user provides series of numerical values for calculator and receives an answer

    # II 1. Investment - user makes decision which of 2 interest calculations to use and calculates return on an investment 
if phrase == "investment":
    print("\nYou have selected an investment: ")
    amount = int(input("\n\tPlease enter amount of money you are depositing.\n\tDeposit value = "))
    interest_rate = float(input("\n\tPlease enter a percentage of an interest rate without \"%\" sign.\n\tPercentage = "))
    years = int(input("\n\tPlease enter number of years you plan on investing.\n\tNumber of years = "))
    loan_type = input("\n\tPlease choose simple or compound type of interest.\n\tSimple or Compound? = ").lower()

    # II 1. a) Simple investment calculation

    if loan_type == "simple":
        calc = amount * ( 1 + ((interest_rate/100) * years))
        print("\n\n\tYour investment will be worth " + str(int(calc)) + "!\n")

    # II 1. b) Compound investment calculation

    elif loan_type == "compound":
        calc = amount * math.pow((1+(interest_rate/100)),years)
        print("\n\n\tYour investment will be worth " + str(int(calc)) + "!\n")

    # II 1. c) Wrong phrase (Neither simple nor compound)

    else:
        print("You entered wrong phrase\n")  
    
    # II 2. Bond - user receives information on the amount of the monthly loan instalment 

elif phrase == "bond":
    print("\nYou have selected a bond: ")
    value = int(input("\n\tPlease provide current value of the house e.g. 1000000. \n\tHouse value = "))
    interest_rate = float(input("\n\tPlease enter a percentage of an interest rate without \"%\" sign e.g. 8: \n\tPercentage = "))
    months = int(input("\n\tPlease enter number of months you plan  to take to repay the bond e.g. 120:\n\tNumber of months = "))
    monthly_percentage = (interest_rate/100)/12
    calc = (monthly_percentage*value)/(1 - (1+monthly_percentage)**(-months))
    print("\n\n\tYou will have to repay " + str(int(calc)) + " each month.\n")

    # III Wrong phrase
else:
    print("You have entered a wrong phrase.\n")