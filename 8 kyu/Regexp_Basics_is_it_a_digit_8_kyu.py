# Regexp Basics - is it a digit?
# Implement String#digit? (in Java StringUtils.isDigit(String)),
# # which should return true if given object is a single digit (0-9), false otherwise.

def is_digit(n):
    if len(n)>1:
        return False
    else:
        return str.isdigit(n)
