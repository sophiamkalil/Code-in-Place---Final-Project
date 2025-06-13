import random

def roll_dice(num_dice):
    dice_values = []

    for i in range(num_dice):
        die_value = random.randint(1, 6)
        dice_values.append(die_value)
    
    return dice_values

def store_die(rolled_dice, stored_dice, index):  # index: index of the rolled dice list to be moved to stored dice
    new_rolled_dice = []
    result = []
    stored_die = rolled_dice[index]
    stored_dice.append(stored_die)

    for i in range(len(rolled_dice)):
        if i != index:
            new_rolled_dice.append(rolled_dice[i])

    result.append(new_rolled_dice)
    result.append(stored_dice)

    return result