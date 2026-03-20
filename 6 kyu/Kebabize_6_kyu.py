# Modify the kebabize function so that it converts a camel case string into a kebab case.

# "camelsHaveThreeHumps"  -->  "camels-have-three-humps"
# "camelsHave3Humps"  -->  "camels-have-humps"
# "CAMEL"  -->  "c-a-m-e-l"
# Notes:

# the returned string should only contain lowercase letters


# def kebabize(s):
#     return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

# import re
# def kebabize(st):
#     result = re.sub(r"([A-Z])", r'-\1', st)
#     result = re.sub(r'\d', '', result)
#     result = re.sub(r'^\-', '', result) 
#     return result.lower()


import re

def kebabize(st):
    return re.sub('\B([A-Z])', r'-\1', re.sub('\d', '', st)).lower()
