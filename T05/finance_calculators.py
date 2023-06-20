import math
# Financial intrest calculator with 2 types of investments, chosen by the user at the beginning of the process

repeat = True
welcome = "\n\nWelcome to the Financial Calculator! Please type in the phrases from the list below:"

while repeat == True:
    # I - Investment/Bond choice Menu
    print(welcome)
    print("\n \t investment" + " - " "to calculate the amount of intrest you'll earn on you investment")
    print("\n \t bond" + "\t    - " "to calculate the amount you'll have to pay on a home loan")
    phrase = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    while True:
        if phrase == "investment" or phrase == "bond":
            break
        else:
            phrase = input("\nWrong phrase, please try only phrases 'Bond' or 'Investment': ")
                

    # II - Calculator - user provides series of numerical values for calculator and receives an answer, if they make mistake
    # they are returned to the beginning of the block "bond" or "investment" they chose at the beginning.

    # User gets confrimation about the choice:

    if phrase == "investment":
        print("\nYou have selected an investment: ")
    else:
        print("\nYou have selected a bond: ")

    # II 1. Investment - user makes decision which of 2 interest calculations to use and calculates return on an investment

    while phrase == "investment":
        try:
            amount = int(input("\nPlease enter amount of money you are depositing, e.g. '100000'.\n\tDeposit value = "))
            interest_rate = float(input("\nPlease enter a percentage of an interest rate without \"%\" sign, e.g. '8'.\n\tPercentage = "))
            years = int(input("\nPlease enter number of years you plan on investing, e.g. '10'.\n\tNumber of years = "))
            loan_type = input("\nPlease choose simple or compound type of interest.\n\tSimple or Compound? = ").lower()
            
            if loan_type == "simple":
                calc = amount * ( 1 + ((interest_rate/100) * years))
                print("\n\nYour investment will be worth " + str(int(calc)) + "!\n")
                break
            elif loan_type == "compound":
                calc = amount * math.pow((1+(interest_rate/100)),years)
                print("\n\nYour investment will be worth " + str(int(calc)) + "!\n")
                break
            else:
                print("Wrong phrase, please try only phrases 'Compound' or 'Simple'.\n")     
        except ValueError:
            print("\nUnexpected sign or phrase, please try over again.")

    # II 2. Bond

    while phrase == "bond":
        try:
            value = int(input("\nPlease provide current value of the house e.g. 1000000. \n\tHouse value = "))
            interest_rate = float(input("\nPlease enter a percentage of an interest rate without \"%\" sign e.g. 8. \n\tPercentage = "))
            months = int(input("\nPlease enter number of months you plan  to take to repay the bond e.g. 120.\n\tNumber of months = "))
            
            monthly_percentage = (interest_rate/100)/12
            
            calc = (monthly_percentage*value)/(1 - (1+monthly_percentage)**(-months))
            print("\n\nYou will have to repay " + str(int(calc)) + " each month.\n")
            break
        except ValueError:
            print("\nUnexpected sign, please try over again")

    # 3. Repeat - User is asked if they want to make another calculation. If Y, calculator starts again. If N, program shuts down.

    continue_cal = input("Thank you for using our calculator!\n\nWould you like to make another calculation?\n\nPlease type 'Y' for yes or 'N' for no: ").lower()

    while True:
        if continue_cal == "y" or continue_cal == "n":
            if continue_cal == "y":
                print("-----------------------------------------------")
                welcome = "\n\nPlease type in the phrases from the list below:"
                break
            else:
                print("\nSee you next time!")
                repeat = False
                break
        else:
            continue_cal = input("\nWrong phrase, please try only phrases 'Y' or 'N':")