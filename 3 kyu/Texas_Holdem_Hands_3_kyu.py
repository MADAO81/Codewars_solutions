# https://www.codewars.com/kata/524c74f855025e2495000262/train/python

def hand(hole_cards, community_cards):
    # Маппинг рангов в числовые значения для сравнения
    rank_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    rank_reverse = {v: k for k, v in rank_map.items()}
    
    all_cards = hole_cards + community_cards
    
    ranks = []
    suits = []
    for card in all_cards:
        rank = card[:-1]
        suit = card[-1]
        ranks.append(rank)
        suits.append(suit)
    
    rank_values = [rank_map[r] for r in ranks]
    
    # Проверка на флеш
    suit_counts = {}
    for s in suits:
        suit_counts[s] = suit_counts.get(s, 0) + 1
    
    flush_suit = None
    for s, count in suit_counts.items():
        if count >= 5:
            flush_suit = s
            break
    
    flush_cards = []
    if flush_suit:
        flush_cards = [(rank_values[i], ranks[i]) for i in range(len(all_cards)) if suits[i] == flush_suit]
        flush_cards.sort(reverse=True)
        flush_ranks = [r[1] for r in flush_cards[:5]]
        flush_values = [r[0] for r in flush_cards]
    
    def find_straight(values):
        # Проверяем все возможные стриты, начиная с самого старшего
        unique_values = sorted(set(values), reverse=True)
        for i in range(len(unique_values) - 4):
            if unique_values[i] - unique_values[i+4] == 4:
                return [rank_reverse[unique_values[i] - j] for j in range(5)]
        return None
    
    def find_best_straight(values):
        # Ищем самый старший стрит
        unique_values = sorted(set(values), reverse=True)
        best_straight = None
        for i in range(len(unique_values) - 4):
            if unique_values[i] - unique_values[i+4] == 4:
                # Это стрит, он будет старше всех следующих
                return [rank_reverse[unique_values[i] - j] for j in range(5)]
        return None
    
    # Считаем повторяющиеся ранги
    rank_count = {}
    for r in rank_values:
        rank_count[r] = rank_count.get(r, 0) + 1
    
    sorted_by_count = sorted(rank_count.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    # Стрит-флеш - проверяем все карты флеша
    if flush_suit:
        # Проверяем все возможные стрит-флеши, берем самый старший
        flush_unique = sorted(set(flush_values), reverse=True)
        for i in range(len(flush_unique) - 4):
            if flush_unique[i] - flush_unique[i+4] == 4:
                straight_flush = [rank_reverse[flush_unique[i] - j] for j in range(5)]
                return "straight-flush", straight_flush
    
    # Каре
    if sorted_by_count[0][1] == 4:
        four_rank = sorted_by_count[0][0]
        remaining = [r for r in rank_values if r != four_rank]
        return "four-of-a-kind", [rank_reverse[four_rank], rank_reverse[max(remaining)]]
    
    # Фулл хаус
    if sorted_by_count[0][1] == 3:
        three_rank = sorted_by_count[0][0]
        pairs = [r for r, count in rank_count.items() if count >= 2 and r != three_rank]
        if pairs:
            pair_rank = max(pairs)
            return "full house", [rank_reverse[three_rank], rank_reverse[pair_rank]]
    
    # Флеш
    if flush_suit:
        return "flush", flush_ranks[:5]
    
    # Стрит
    straight = find_best_straight(rank_values)
    if straight:
        return "straight", straight
    
    # Трипс
    if sorted_by_count[0][1] == 3:
        three_rank = sorted_by_count[0][0]
        remaining = [r for r in rank_values if r != three_rank]
        remaining = sorted(set(remaining), reverse=True)[:2]
        return "three-of-a-kind", [rank_reverse[three_rank]] + [rank_reverse[r] for r in remaining]
    
    # Две пары
    pairs = [r for r, count in rank_count.items() if count == 2]
    if len(pairs) >= 2:
        pairs_sorted = sorted(pairs, reverse=True)[:2]
        high_pair = pairs_sorted[0]
        low_pair = pairs_sorted[1]
        remaining = [r for r in rank_values if r != high_pair and r != low_pair]
        kicker = max(remaining)
        return "two pair", [rank_reverse[high_pair], rank_reverse[low_pair], rank_reverse[kicker]]
    
    # Пара
    if sorted_by_count[0][1] == 2:
        pair_rank = sorted_by_count[0][0]
        remaining = [r for r in rank_values if r != pair_rank]
        remaining = sorted(set(remaining), reverse=True)[:3]
        return "pair", [rank_reverse[pair_rank]] + [rank_reverse[r] for r in remaining]
    
    # Ничего
    top_cards = sorted(set(rank_values), reverse=True)[:5]
    return "nothing", [rank_reverse[r] for r in top_cards]
