# Switch it Up!
# When provided with a number between 0-9, return it in words. 
# Note that the input is guaranteed to be within the range of 0-9.
# Input: 1
# Output: "One".
# If your language supports it, try using a switch statement.


    
# def switch_it_up(number):
#     return {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
#             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}.get(number)

def switch_it_up(number):
    numbers = {"Zero":0, "One":1,"Two":2, "Three":3,
              "Four":4, "Five":5, "Six":6, "Seven":7,
              "Eight":8, "Nine":9}
    return next(key for key, value in numbers.items() if value == number)
