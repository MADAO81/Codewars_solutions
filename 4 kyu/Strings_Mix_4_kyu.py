# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python


# def mix(s1, s2):
#     s = []
#     lett = "abcdefghijklmnopqrstuvwxyz"
#     for ch in lett:
#         val1, val2 = s1.count(ch), s2.count(ch)
#         if max(val1, val2) >= 2:
#             if val1 > val2: s.append("1:"+val1*ch)
#             elif val1 < val2: s.append("2:"+val2*ch)
#             else: s.append("=:"+val1*ch)
            
#     s.sort()
#     s.sort(key=len, reverse=True)
#     return "/".join(s)


def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
