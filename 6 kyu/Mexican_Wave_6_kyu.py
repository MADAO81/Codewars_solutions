# Mexican Wave
# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
# You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
# Rules
#  1.  The input string will always be lower case but maybe empty.

#  2.  If the character in the string is whitespace then pass over it as if it was an empty seat
# Example
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]



# def wave(people):
#     result = []
#     for indx, char in enumerate(people):
#         if char == " ":
#             pass
#         else:
#             el_people = list(people)
#             el_people[indx] = el_people[indx].upper()
#             el_people = "".join(el_people)
#             result.append(el_people)
#     return result



def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
