# https://www.codewars.com/kata/5356ad2cbb858025d800111d
# Name Array Capping
# Create a function that accepts an array of names, and returns 
# an array of each name with its first letter capitalized and the remainder in lowercase.

# Examples
# ['jo', 'nelson', 'jurie'] -->  ['Jo', 'Nelson', 'Jurie']
# ['KARLY', 'DANIEL', 'KELSEY'] --> ['Karly', 'Daniel', 'Kelsey']


# def cap_me(arr):
#     result = []
#     for ch in arr:
#         if ch == "":
#             result.append(ch)
#         else:
#             result.append(ch[0].upper()+ch[1:].lower())
#    return result



# def cap_me(arr):
#     return list(map(str.title, arr))



def cap_me(arr):
    return [name.capitalize() for name in arr]
