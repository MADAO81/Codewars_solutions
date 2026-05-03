# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"


def people_with_age_drink(age):
    return {
        'kids': "drink toddy",
        'teens': "drink coke",
        'young': "drink beer",
        'adults': "drink whisky"
    } ['kids' if age < 14 else 'teens' if age < 18 else 'young' if age < 21 else 'adults']


def people_with_age_drink(age):
    if age <= 13:
        beverage = 'toddy'
    elif age > 13 and age <= 17:
        beverage = 'coke'
    elif age > 17 and age <= 20:
        beverage = 'beer'
    elif age > 20:
        beverage = 'whisky'
    return 'drink ' + beverage
