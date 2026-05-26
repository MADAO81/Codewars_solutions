# https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python


# import collections
# import re

# def parse_molecule(formula):
#     for r in r'\(([^\)]+)\)(\d+)', r'\[([^\]]+)\](\d+)', r'\{([^\}]+)\}(\d+)', r'([A-Z][a-z]?)(\d+)':
#         formula = re.sub(r, lambda pair:''.join(pair.group(1)for _ in range(int(pair.group(2)))), formula)
#     ravel = re.findall(r'[A-Z][a-z]?', formula)
#     ret = collections.Counter(ravel)
#     return dict(ret)



from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts
