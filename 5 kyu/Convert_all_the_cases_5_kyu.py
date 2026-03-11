# In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.

# You must write a function that changes to a given case. It must be able to handle all three case types:

# py> change_case("snakeCase", "snake")
# "snake_case"
# py> change_case("some-lisp-name", "camel")
# "someLispName"
# py> change_case("map_to_all", "kebab")
# "map-to-all"
# py> change_case("doHTMLRequest", "kebab")
# "do-h-t-m-l-request"
# py> change_case("invalid-inPut_bad", "kebab")
# None
# py> change_case("valid-input", "huh???")
# None
# py> change_case("", "camel")
# ""
# Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase.

# (Any translations would be greatly appreciated!)



# import re
# def change_case(identifier, target_case):
#     regex = re.compile(r"[A-Z]?[a-z]*")
    
#     if "-" in identifier and identifier.islower():
#         mo = identifier.split("-")
#     elif "_" in identifier and identifier.islower():
#         mo = identifier.split("_")
#     elif "-" not in identifier and not "_" in identifier:
#         mo = regex.findall(identifier)
#     else:
#         return None
    
#     for element in mo:
#         if len(element) == 0:
#             mo.pop(mo.index(element))
#         elif element.isalpha():
#             continue
#         else:
#             return None
        
#     if target_case == "snake":
#         return "_".join(mo).lower()
#     elif target_case == "kebab":
#         return "-".join(mo).lower()
#     elif target_case == "camel":
#         for index in range(1, len(mo)):
#             mo[index] = mo[index].title()
#         return "".join(mo)
#     else:
#         return None



import re

def change_case(label, target):
    if ('_' in label) + ('-' in label) + (label != label.lower()) > 1:
        return
    
    if target == 'snake':
        return re.sub('([A-Z])', r'_\1', label.replace('-', '_')).lower()
    
    if target == 'kebab':
        return re.sub('([A-Z])', r'-\1', label.replace('_', '-')).lower()
    
    if target == 'camel':
        return re.sub('([_-])([a-z])', lambda m: m.group(2).upper(), label)

