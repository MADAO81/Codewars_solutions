#https://www.codewars.com/kata/59b9a92a6236547247000110/train/python


Solution #1
# from math import factorial as fac
# cards = [
#     "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC",
#     "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD",
#     "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
#     "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"
# ]
# symbols = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# symbols_len = len(symbols)
# facs = [1]
# for x in range(1, 53, 1):
#     facs.append(facs[-1] * x)



# class PlayingCards:
#     def encode(self, message):
#         mess_len = len(message)
#         rem = 0
#         for i in range(mess_len):
#             if message[i] not in symbols: return None
#             rem = rem + symbols_len ** (mess_len - i - 1) * symbols.index(message[i])
#         if rem >= facs[-1]: return None
#         for i in range(1, 53):
#             if rem < facs[i]: break
#         remaining_cards = cards[53 - i - 1:]
#         cards_o = cards[:53 - i - 1]
#         for j in range(i - 1, -1, -1):
#             idx = rem // facs[j]
#             cards_o.append(remaining_cards.pop(idx))
#             rem = rem % facs[j]
#         return cards_o


#     def decode(self, deck):
#         if len(deck) != 52: return None
#         remaining_cards = cards.copy()
#         rem = 0
#         for i in range(len(deck)):
#             if deck[i] not in remaining_cards: return None
#             idx = remaining_cards.index(deck[i])
#             rem = rem + facs[51 - i] * idx
#             remaining_cards.pop(idx)
#         res = []

#         if rem == 0 :
#             return ''

#         while rem > 0:
#             res.insert(0, symbols[rem % symbols_len])
#             rem = rem // symbols_len

#         return ''.join(res)


Solution # 2

from math import factorial
from numpy import base_repr
from string import ascii_uppercase, digits

class PlayingCards:
    DECK  = [rank + suit for suit in 'CDHS' for rank in 'A23456789TJQK']
    RANKS = {card: rank for rank, card in enumerate(DECK)}
    FACTS = list(map(factorial, range(len(DECK) - 1, -1, -1)))

    CHARSET,   BASE27      = ' ' + ascii_uppercase, (digits + ascii_uppercase)[:27]
    TO_BASE27, FROM_BASE27 = str.maketrans(CHARSET, BASE27), str.maketrans(BASE27, CHARSET)

    def encode(self, text: str) -> list or None:
        if not text: return self.DECK.copy()
        if not set(text) <= set(self.CHARSET): return None
        n = int(text.translate(self.TO_BASE27), 27)                         # Heptavigesimal -> Decimal
        if n >= self.FACTS[0] * 52: return None
        cards = self.DECK.copy()
        nth_perm = []                                                       # Nth (Lexicographic) Permutation
        for fact in self.FACTS:
            cycles, n = divmod(n, fact)
            nth_perm.append(cards.pop(cycles))
        return nth_perm

    def decode(self, deck: list) -> str or None:
        if set(deck) != self.RANKS.keys(): return None
        n = sum(self.FACTS[i] * sum(self.RANKS[right] < self.RANKS[card] for right in deck[i + 1:])
                for i, card in enumerate(deck))                             # Lexicographic Rank
        return base_repr(n, 27).translate(self.FROM_BASE27) if n else ''    # Decimal -> Heptavigesimal
