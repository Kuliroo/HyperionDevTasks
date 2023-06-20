# Program which calculates stock value based on list of stock items and two dictionaries including their respective stock level and price

# Variables
menu = ['coffee', 'tea', 'cookie', 'muffin']
stock = {menu[0]: 1000, menu[1]: 980, menu[2]: 20, menu[3]: 50}
price = {menu[0]: 2.40, menu[1]: 2.70, menu[2]: 2.90, menu[3]: 2.50}
currency = '£'
total_value = 0

# for loop to calculate values

for i in menu:
    item_value = (stock[i] * price[i])
    '''print(f'The value of {i} is {currency}{item_value}')''' #part which allows to display stock value of each item
    total_value += item_value
print(f'Total value of the stock is: {currency}{total_value}')