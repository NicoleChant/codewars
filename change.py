# Welcome young Jedi! 
# In this Kata you must create a function that takes an amount of US currency in cents, 
# and returns a dictionary/hash which shows the least amount of coins used to make up that 
# ount. 
# The only coin denominations considered in this exercise are: 
# Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢). 
# Therefore the dictionary returned should contain exactly 4 key/value pairs.

#Notes:

# If the function is passed either 0 or a negative number, the function should 
# return the dictionary with all values equal to 0.
# If a float is passed into the function, its value should be be rounded down, 
# and the resulting dictionary should never contain fractions of a coin.

def loose_change(cents):
    change_dict = {"Nickels":0, "Pennies":0, "Dimes":0, "Quarters":0}
    if cents <=0 :
        return change_dict
    cents = int(cents)
    partition = {"Quarters":25,"Dimes":10,"Nickels":5,"Pennies":1}
    for key , value in partition.items():
        num = cents//value
        cents = cents%value
        change_dict[key] += num 
        if cents == 0: return change_dict 
    return change_dict

def main():
    cents = 56.7
    print(loose_change(cents))

if __name__ == "__main__" : main()