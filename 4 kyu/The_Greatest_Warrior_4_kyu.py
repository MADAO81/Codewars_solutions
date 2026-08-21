# https://www.codewars.com/kata/5941c545f5c394fef900000c/train/python

class Warrior:
    def __init__(self):
        self._experience = 100
        self._level = 1
        self._rank_index = 0
        self._achievements = []
        self._ranks = [
            "Pushover", "Novice", "Fighter", "Warrior", "Veteran",
            "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"
        ]
        self._update_rank()

    @property
    def experience(self):
        return self._experience

    @property
    def level(self):
        return self._level

    @property
    def rank(self):
        return self._ranks[self._rank_index]

    @property
    def achievements(self):
        return self._achievements.copy()

    def _update_level_and_rank(self):
        # Update level based on experience
        new_level = self._experience // 100
        if new_level > 100:
            new_level = 100
        self._level = new_level
        self._update_rank()

    def _update_rank(self):
        # Update rank based on current level
        if self._level == 100:
            self._rank_index = 10  # "Greatest"
        else:
            # Levels 1-9 -> index 0 (Pushover)
            # Levels 10-19 -> index 1 (Novice)
            # Levels 20-29 -> index 2 (Fighter), etc.
            self._rank_index = self._level // 10

    def _get_rank_index(self, level):
        if level == 100:
            return 10
        return level // 10

    def battle(self, enemy_level):
        # Validate enemy level
        if not 1 <= enemy_level <= 100:
            return "Invalid level"

        # Check if warrior can fight (rank and level difference check)
        # This must be checked BEFORE any experience is applied
        if (self._get_rank_index(enemy_level) > self._rank_index and 
            enemy_level - self._level >= 5):
            return "You've been defeated"

        # Calculate experience gained
        diff = enemy_level - self._level
        if diff == 0:
            xp_gain = 10
        elif diff == -1:
            xp_gain = 5
        elif diff <= -2:
            xp_gain = 0
        else:  # diff >= 1
            xp_gain = 20 * diff * diff

        # Update experience (capped at 10000)
        self._experience = min(self._experience + xp_gain, 10000)
        self._update_level_and_rank()

        # Determine fight response
        if diff <= -2:
            return "Easy fight"
        elif diff in (-1, 0):
            return "A good fight"
        else:  # diff >= 1
            return "An intense fight"

    def training(self, training_data):
        description, xp_gain, min_level = training_data

        if self._level < min_level:
            return "Not strong enough"

        self._experience = min(self._experience + xp_gain, 10000)
        self._update_level_and_rank()
        self._achievements.append(description)
        return description
