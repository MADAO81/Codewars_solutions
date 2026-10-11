# Accountant time! For a given quantity and price (per mango), calculate the total cost of the mangoes.
# But! Every third mango is free!

def mango(quantity, price):
    return (quantity - quantity//3)*price
