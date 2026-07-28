# Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0.

# def combat(health, damage):
#     result = health - damage
#     if result < 0:
#         return 0
#     return result


def combat(health, damage):
    return health - damage if health > damage else 0
