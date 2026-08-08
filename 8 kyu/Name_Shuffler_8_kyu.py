# Name Shuffler
# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"

# def name_shuffler(str_):
#     oper = str_.split()
#     oper1 = oper[::-1]
#     return " ".join(oper1)
    
def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])
