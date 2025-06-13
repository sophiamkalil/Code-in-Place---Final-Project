import random

def roll_dice(num_dice):
    dice_values = []

    for i in range(num_dice):
        die_value = random.randint(1, 6)
        dice_values.append(die_value)
    
    return dice_values