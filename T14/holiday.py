# A program which takes 3 inputs from the user: destination, number of nights, number of car rental days and
# returns a cost of a holiday to particular destination, together with stay and transportation cost

# Function to calculate cost of the hotel stay
def hotel_cost(x):
            hotel_per_night = 65
            return x * hotel_per_night
# Function to determine flight cost
def plane_cost(x):
    while True:
        if  x == "rome":
            return 80
        elif x == "london":
            return 40
        elif x == "paris":
            return 60
        else:
            x = input("Please choose from the options above: ").lower()
# Function to calculate cost of the car rental
def car_rental(x):
    car_rental_per_day = 24
    return x * car_rental_per_day
# Function to calculate total cost of the holiday
def holiday_cost(x,y,z):
    return x + y + z
# Function to check if user provides integer where needed
def is_integer(x):
    while True:
        try:
              is_number = int(x)
        except ValueError:
             x = input("Please, provide a number: ")
             continue
        else:
            return is_number

# Welcome message
print("Welcome to the holiday calculator! Please choose destination from the list below: \n- London\n- Rome\n- Paris")

# Flight cost
city_flight = input("Please state the destination: ").lower()
x = plane_cost(city_flight)
print(f"The cost of the chosen flight destination would be £{x}.")
# Hotel cost
num_nights = is_integer(input("Please state the number of nights that you wish to stay in: "))
y = hotel_cost(num_nights)
print(f"The cost of the hotel would be £{y}.")
# Rental cost
rental_days = is_integer(input("Please state the number of days you wish to rent the car for: "))
z = car_rental(rental_days)
print(f"The cost of the car rental would be £{z}.")
# Total cost
print(f"The total cost of your holiday would be £{holiday_cost(x,y,z)}.")
