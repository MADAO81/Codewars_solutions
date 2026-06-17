# https://www.codewars.com/kata/5882b052bdeafec15e0000e6/train/python

# class Quark(object):
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#         self.baryon_number = 1/3
        
#     def interact(self, other):
#         self.color, other.color = other.color, self.color


class Quark(object):
    _COLOR = frozenset(["red", "blue", "green"])
    _FLAVOR = frozenset(['up', 'down', 'strange', 'charm', 'top', 'bottom'])
    baryon_number = 1 / 3

    def __init__(self, color, flavor):
        if color in self._COLOR:
            self.color = color
        else:
            raise ValueError(f"{color} is not allowed color for quarks!")
        if flavor in self._FLAVOR:
            self.flavor = flavor
        else:
            raise ValueError(f"{flavor} is not allowed flavor for quarks!")

    def interact(self, quark):
        self.color, quark.color = quark.color, self.color
