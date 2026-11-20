# Write a simple regex to validate a username. Allowed characters are:

# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).



# import re
# def validate_usr(un):
#     return re.match('^[a-z0-9_]{4,16}$', un) != None

import re
def validate_usr(username):
    pattern = re.compile(f"^[a-z0-9_]{{{4},{15}}}$")
    return bool(pattern.match(username))
