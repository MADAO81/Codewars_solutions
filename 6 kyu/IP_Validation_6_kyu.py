# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string



# import socket

# def is_valid_IP(addr):
#     try:
#         socket.inet_pton(socket.AF_INET, addr)
#         return True
#     except socket.error:
#         return False


# def is_valid_IP(s):
#     return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))



from ipaddress import ip_address
def is_valid_IP(strng):
    try:
        return True if ip_address(strng) else False
    except:
        return False
