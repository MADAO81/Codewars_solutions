# https://www.codewars.com/kata/58b57ae2724e3c63df000006/train/python

# def parse_html_color(color):
#     rgb = []
#     if not color.startswith('#'):
#         color = PRESET_COLORS[color.lower()]

#     color = color[1:]
#     if len(color) == 3:
#         for ch in color:
#             rgb.append(int(ch + ch, 16))
#     elif len(color) == 6:
#         for i in range(0, 6, 2):
#             rgb.append(int(color[i:i + 2], 16))

#     return dict(zip('rgb', rgb))


def parse_html_color(color):
    color = PRESET_COLORS.get(color.lower(), color)
    
    if len(color) == 7:
        r, g, b = (int(color[i:i+2], 16) for i in range(1, 7, 2))
    else:
        r, g, b = (int(color[i+1]*2, 16) for i in range(3))
    
    return dict(zip("rgb", (r, g, b)))
