# https://www.codewars.com/kata/52fea6fd158f0576b8000089/train/python

# import binascii

# class Converter():
#     @staticmethod
#     def to_ascii(h):
#         return binascii.unhexlify(h).decode()
#     @staticmethod
#     def to_hex(s):
#         return binascii.hexlify(s.encode()).decode()


class Converter():
    def to_ascii(h):
        return bytes.fromhex(h).decode()
    
    def to_hex(s):
        return s.encode().hex()
