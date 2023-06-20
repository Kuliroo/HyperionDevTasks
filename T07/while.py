sum = 0
count = 0
number = int(input("\nPlease enter a number, if you enter -1 you will get an average of previous numbers: "))

while number != -1:
    sum += number
    count += 1
    number = int(input("\nPlease enter a number, if you enter -1 you will get an average of previous numbers: "))
else:
    average = sum/count
    print("Your average is: " + str(average) + ".")