# https://www.codewars.com/kata/567fe8b50c201947bc000056/train/python

# import ipaddress

# def ipv4_address(address):
#     try:
#         ipaddress.ip_address(address)
#         return True
#     except ValueError:
#         return False


# import socket
# def ipv4_address(address):
#     try: # No need to do work that's already been done
#         socket.inet_pton(socket.AF_INET,address)
#         return True
#     except socket.error: # Better to ask forgiveness than permission
#         return False



from re import compile, match

REGEX = compile(r'((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){4}$')


def ipv4_address(address):
    # refactored thanks to @leonoverweel on CodeWars
    return bool(match(REGEX, address + '.'))
