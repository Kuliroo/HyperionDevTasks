# Program that validates if user has put at least two names while entering his full name, based on provided error messages
name=input("Hello, please provide your full name: \n")
'''
using len() function to determine lenght of the name, 
then if statements for particular amount of signs 
which might indicate the wrong answer. 
'''
if len(name) == 0:
    print("You haven't entered anything. Please enter your name.")
elif len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname")
elif len(name) >25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name")