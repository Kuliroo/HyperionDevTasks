import math

# A program which asks user to 1. Enter a file name (once) and then to perform calculation on two numbers.; 2. Read the contents of the created file.

# Defining functions for the program

    # Calculator function checking if the number is a float
    # I have received information about def and this particular way of checking if something is a float from 1:1 call with mentor Leon Stevens.

def calculator():
    number = input()
    is_number = False
    while is_number == False:
        try:
            float(number)
            is_number = True
        except ValueError:
            is_number = False

        if is_number:
            return number
        number = input("Please enter a number:")

    # Memory function to write down the equations into the txt file (looked up on w3)

def memory():
    f = open(f"{file_name}.txt", "a")
    f.write(f"{checked_number_1} {operator} {checked_number_2} = {equation}\n")
    f.close()

    # [Program] Restart function to either return user to the beginning of the program or to finish it

def restart():
    global repeat
    global welcome
    while True:
        continue_cal = input("\nWould you like to return to the title screen?\n\nPlease type 'Y' for yes or 'N' for no: ").lower()
        if continue_cal == "y" or continue_cal == "n":
            if continue_cal == "y":
                print("-"*20)
                break
            else:
                print("\nSee you next time!")
                repeat = False
                break
        else:
            continue_cal = input("\nWrong phrase, please try only phrases 'Y' or 'N':")

repeat = True  #boolean to start while loop but allow to stop the loop if user decides to stop the program at certain points
welcome = "Please follow the instructions:\n"
file_name = ""
file_name_bool = True
first_use = 0
while repeat:
    if first_use == 0:
        print("\n\nWelcome to the calculator!\n\n")
    first_use += 1
    options = input("Please choose from the two options below:\n\n1. Create a file to store your calculations (only once), then enter two numbers and operator to receive a result of an equation.\n\n2. Read all previous equations from a memory file. \n\n Option: ")
    if options == "1":       
        
        # CALCULATOR

        while True:

            print(f"\n{welcome}")
            if not file_name:
                file_name = input("\nPlease choose a name for a file that will store the results of your equations:\t")
            print("\nPlease enter a First number: ")
            checked_number_1 = float(calculator())

            print("\nPlease provide an operator: ")
            operator = input()
            
            print("\nPlease enter a Second number: ")
            checked_number_2 = float(calculator())

            while True:

                    if operator == '+':
                        equation = checked_number_1+checked_number_2
                        print(f"\nResult of the equation is: {equation}")
                        memory()
                        break
                    elif operator == '-':
                        equation = checked_number_1-checked_number_2
                        print(f"\nResult of the equation is: {equation}")
                        memory()
                        break
                    elif operator == '*':
                        equation = checked_number_1*checked_number_2
                        print(f"\nResult of the equation is: {equation}")
                        memory()
                        break
                    elif operator == '/':
                        while True:
                            if checked_number_2 == 0:
                                print("\n You can't divide by 0, please provide other number: ")
                                checked_number_2 = float(calculator())
                            else:
                                equation = checked_number_1/checked_number_2
                                print(f"\nResult of the equation is: {equation}")
                                memory()
                                break
                        break
                    else:
                        operator = input("\nPlease provide one of the listed operators '+, -, *, / ': \n")

            # Loop that allows user to start another equation or close the calculator
            restart()
            break

    elif options == "2":
        count = 1
        file_name_bool = True

        while file_name_bool:
                file_name_check = input("\nPlease provide a name of the file with your stored calculations:\n")
                if not file_name:
                    print("\nThere is no file with stored calculations. Please return to main screen and perform some calculations first.\n")
                    break
                elif file_name_check == file_name:
                    file_name_bool = False
                    f = open(f"{file_name}.txt")
                    print("\nPreviously stored equations:\n")
                    print(f.read())
                    f.close()
                    count = 0
                    restart()
                elif count == 3:
                    print("!"*3)
                    print(f"You have entered the wrong file name three times, maybe try: {file_name}")
                    print("!"*3)
                    break
                else:
                    print("File seems to not exist.\n")
                    count += 1
    else:
        print("\nPlease state correct option, either 1 or 2.\n")