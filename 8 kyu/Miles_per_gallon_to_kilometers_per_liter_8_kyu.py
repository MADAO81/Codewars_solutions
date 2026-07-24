# Sometimes, I want to quickly be able to convert miles per imperial gallon (mpg) into kilometers per liter (kpl).

# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).

# Make sure to round off the result to two decimal points.

# Some useful associations relevant to this kata:

# 1 Imperial Gallon = 4.54609188 litres
# 1 Mile = 1.609344 kilometres

def converter(mpg):
    gallons_to_liters = 4.54609188
    miles_to_kilometers = 1.609344
    # Calculate kilometers per liter
    kpl = mpg * (miles_to_kilometers / gallons_to_liters)
    # Round the result to two decimal places
    return round(kpl, 2)
