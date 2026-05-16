# https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python


# def sq_in_rect(lng, wdth):
#     if lng == wdth:
#         return None
#     short,long = sorted((lng,wdth))
#     result = []
#     while short != long:
#         result.append(short)
#         long -= short
#         short, long = sorted((short,long))
#     result.append(short)
#     return result

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res
