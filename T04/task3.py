# A program to determine awards for people taking part in triathlon competition

'''
I wasn't sure about the part "The qualifying time for awards is 100 minutes". There are two awards for 5
and 10 minutes "within of qualifying time". To me it sounds like, if you "barely made it" in either 105 or 110 minutes
you still get the award (I assume Half Colours are worse than Colours). If it should be the other way, that the best 
times of <90 and <95 minutes are rewarded better, it can be easily done by replacing values in particular awards.
I did it the way I understood the award system works based on value of the awards, but due to that people are getting
awarded for times >100, making "The qualifying time for awards is 100 minutes" false. Not sure if it was catch or
just simply misunderstanding.
'''
# Asking for each individual time, using float as I understand that 100 minutes is still "in time" but 100.1 minutes is not
print("Thank you for taking part in our Triathlon Competition, please provide your times for each event in minutes.")
swim = float(input("\nPlease let us know how long did it take for you to finish the swimming event: "))
cycle = float(input("\nPlease let us know how long did it take for you to finish the cycling event: "))
run = float(input("\nPlease let us know how long did it take for you to finish the running event: "))

time = swim + cycle + run
qualifying_time = 100

# Prize for <= 100 minutes
if time <= qualifying_time:
    print("\nCongratulations you have completed the triathlon in the qualifying time of " + str(time) + " minutes !\nYour award is Provincial Colours!")

# Prize for <= 105 minutes
elif time <= qualifying_time + 5:
    print("\nWell done! You almost made it in qualifying time, but it took you " + str(time) + " minutes! \nYour award is Provincial Half Colours!")
# Prize for <= 110 minutes
elif time <= qualifying_time + 10:
    print("\nNot bad! Good luck next time, it took you " + str(time) +" minutes! \nYour award is Provincial Scroll!")
# No prize for the rest of times
else:
    print("\nIt took you a bit too much time, exactly " + str(time) +" minutes! \nThere is no award for you, sorry!")