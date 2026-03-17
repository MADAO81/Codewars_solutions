# Pluralization
# Your code should take an English noun with a regular plural form and return its plural.

# Rules for pluralization in English:

# If a singular noun ends in '-s', '-x', '-z', '-ch' or '-sh', add '-es'

# If a singular noun ends with a consonant and '-y', change '-y' to '-ies'.

# All other words just add '-s'

# None of the tests end in '-f' or '-o' and none are irregular nouns (e.g. child, mouse etc.)

# Examples

# table -> tables,
# window -> windows,
# church -> churches,
# watch -> watches,
# bus -> buses,
# box -> boxes,
# buzz -> buzzes,
# fly -> flies


def pluralize(word):
    consonants = "bcdfghjklmnpqrstvwxyz"
    plural_rule = ("s", "x", "z", "ch", "sh")
    for rule in plural_rule:
        if word[-2:] == "ch" or word[-2:] == "sh":
            return word + "es"
        elif word[-1:] == "s" or word[-1:] == "x" or word[-1:] == "z":
            return word + "es"
    for letter in consonants:
        if word.endswith(f"{letter}y"):
            return f"{word[:-1]}ies"
    return f"{word}s"


