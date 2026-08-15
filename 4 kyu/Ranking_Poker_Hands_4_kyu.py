# https://www.codewars.com/kata/5739174624fc28e188000465/train/python


from collections import Counter

class PokerHand:
    RESULT = ["Loss", "Tie", "Win"]
    
    # Ранги карт (от 2 до A)
    RANK_ORDER = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                  '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    def __init__(self, hand):
        self.cards = hand.split()
        self.ranks = sorted([self.RANK_ORDER[card[0]] for card in self.cards], reverse=True)
        self.suits = [card[1] for card in self.cards]
        self.rank_counts = Counter(self.ranks)
        self.rank_values = sorted(self.rank_counts.values(), reverse=True)
        
        # Проверка на стрит (учитывая низкий туз)
        self.is_straight = self._check_straight()
        self.is_flush = len(set(self.suits)) == 1
        
        # Определение типа руки
        self.hand_type = self._get_hand_type()
        # Ключи для сравнения рук
        self.hand_key = self._get_hand_key()
    
    def _check_straight(self):
        """Проверка на стрит (с учетом низкого туза)"""
        unique_ranks = sorted(set(self.ranks), reverse=True)
        if len(unique_ranks) < 5:
            return False
        
        # Обычный стрит
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i] - unique_ranks[i+4] == 4:
                return True
        
        # Стрит с низким тузом (A, 2, 3, 4, 5)
        if set([14, 2, 3, 4, 5]).issubset(set(self.ranks)):
            return True
        
        return False
    
    def _get_hand_type(self):
        """Определение типа руки (числовое значение для сравнения)"""
        if self.is_flush and self.is_straight:
            # Проверка на роял-флеш (туз-король-дама-валет-10)
            if set([10, 11, 12, 13, 14]).issubset(set(self.ranks)):
                return 9  # Роял-флеш
            return 8  # Стрит-флеш
        
        if 4 in self.rank_values:
            return 7  # Каре
        
        if 3 in self.rank_values and 2 in self.rank_values:
            return 6  # Фулл-хаус
        
        if self.is_flush:
            return 5  # Флеш
        
        if self.is_straight:
            return 4  # Стрит
        
        if 3 in self.rank_values:
            return 3  # Сет (тройка)
        
        if self.rank_values.count(2) == 2:
            return 2  # Две пары
        
        if 2 in self.rank_values:
            return 1  # Одна пара
        
        return 0  # Старшая карта
    
    def _get_hand_key(self):
        """Создание ключа для сравнения рук одного типа"""
        if self.hand_type == 9:  # Роял-флеш
            return [14]
        
        if self.hand_type == 8:  # Стрит-флеш
            return self._get_straight_high()
        
        if self.hand_type == 7:  # Каре
            four_rank = [r for r, c in self.rank_counts.items() if c == 4][0]
            kicker = [r for r, c in self.rank_counts.items() if c == 1][0]
            return [four_rank, kicker]
        
        if self.hand_type == 6:  # Фулл-хаус
            three_rank = [r for r, c in self.rank_counts.items() if c == 3][0]
            two_rank = [r for r, c in self.rank_counts.items() if c == 2][0]
            return [three_rank, two_rank]
        
        if self.hand_type == 5:  # Флеш
            return sorted(self.ranks, reverse=True)
        
        if self.hand_type == 4:  # Стрит
            return self._get_straight_high()
        
        if self.hand_type == 3:  # Сет
            three_rank = [r for r, c in self.rank_counts.items() if c == 3][0]
            kickers = sorted([r for r, c in self.rank_counts.items() if c == 1], reverse=True)
            return [three_rank] + kickers
        
        if self.hand_type == 2:  # Две пары
            pairs = sorted([r for r, c in self.rank_counts.items() if c == 2], reverse=True)
            kicker = [r for r, c in self.rank_counts.items() if c == 1][0]
            return pairs + [kicker]
        
        if self.hand_type == 1:  # Одна пара
            pair_rank = [r for r, c in self.rank_counts.items() if c == 2][0]
            kickers = sorted([r for r, c in self.rank_counts.items() if c == 1], reverse=True)
            return [pair_rank] + kickers
        
        # Старшая карта
        return sorted(self.ranks, reverse=True)
    
    def _get_straight_high(self):
        """Получение старшей карты стрита (с учетом низкого туза)"""
        unique_ranks = sorted(set(self.ranks), reverse=True)
        
        for i in range(len(unique_ranks) - 4):
            if unique_ranks[i] - unique_ranks[i+4] == 4:
                return [unique_ranks[i]]
        
        # Низкий стрит (A, 2, 3, 4, 5)
        if set([14, 2, 3, 4, 5]).issubset(set(self.ranks)):
            return [5]  # Старшая карта - 5
        
        return [max(self.ranks)]
    
    def compare_with(self, other):
        """Сравнение с другой рукой"""
        if self.hand_type > other.hand_type:
            return self.RESULT[2]  # Win
        if self.hand_type < other.hand_type:
            return self.RESULT[0]  # Loss
        
        # Одинаковые типы рук - сравниваем ключи
        for self_val, other_val in zip(self.hand_key, other.hand_key):
            if self_val > other_val:
                return self.RESULT[2]  # Win
            if self_val < other_val:
                return self.RESULT[0]  # Loss
        
        return self.RESULT[1]  # Tie
