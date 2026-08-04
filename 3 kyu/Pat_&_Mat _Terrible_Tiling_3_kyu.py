# https://www.codewars.com/kata/6984a5b68a60d5883c63b902/train/python

def find_missing_tiles(width, height, tiles):
    tiles = sorted([(width, 0, 0, height), *tiles])
    ys = sorted({y for _, y0, _, h in tiles for y in [y0, y0 + h]})
    xs = [0] * len(ys)
    indices = {y: i for i, y in enumerate(ys)}
    res = set()
    
    for x, y, w, h in tiles:
        for i in range(indices[y], indices[y + h]):
            if xs[i] < x:
                # Добавляем клетки, но не больше 200
                for u in range(xs[i], x):
                    for v in range(ys[i], ys[i + 1]):
                        res.add((u, v))
                        if len(res) >= 200:
                            return res
            xs[i] = x + w
            # Если уже нашли 200, можно выйти
            if len(res) >= 200:
                return res
    
    return res
