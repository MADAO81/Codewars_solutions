# https://www.codewars.com/kata/590adadea658017d90000039/train/python

def fruit(reels, spins):
    symbols = [reels[i][spins[i]] for i in range(3)]
    
    coeff = {'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 
             'Seven': 6, 'Cherry': 5, 'Bar': 4, 'King': 3, 
             'Queen': 2, 'Jack': 1}
    
    # Считаем символы
    counts = {}
    for s in symbols:
        counts[s] = counts.get(s, 0) + 1
    
    # Сортируем по убыванию количества
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    # Если все 3 одинаковые
    if len(sorted_counts) == 1:
        sym = sorted_counts[0][0]
        if sym == 'Wild':
            return 100  # 10 * 10
        return coeff[sym] * 10
    
    # Если есть 2 одинаковых
    if sorted_counts[0][1] == 2:
        sym = sorted_counts[0][0]
        
        # Случай: 2 Wild + 1 другой
        if sym == 'Wild':
            return coeff['Wild']  # = 10
        
        # Случай: 2 одинаковых (не Wild) + 1 Wild
        if 'Wild' in counts and counts['Wild'] == 1:
            return coeff[sym] * 2  # Бонус за Wild
        
        # Случай: 2 одинаковых без Wild
        return coeff[sym]
    
    # Все разные
    return 0
