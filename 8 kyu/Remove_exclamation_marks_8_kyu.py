# Remove exclamation marks
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    symbol_to_remove = "!"
    return ("".join(char for char in s if char not in symbol_to_remove))
