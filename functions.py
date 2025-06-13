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

def remove_die(rolled_dice, stored_dice, index):  # index: index of the stored dice list to be removed and moved to rolled dice
    result = []
    updated_stored_dice = []
    removed_die = stored_dice[index]
    rolled_dice.append(removed_die)

    for i in range(len(stored_dice)):
        if i != index:
            updated_stored_dice.append(stored_dice[i])

    result.append(rolled_dice)
    result.append(updated_stored_dice)

    return result

def calculate_simple_rule_points(dice_faces):
    points = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    for face in dice_faces:
        if face in points:
            points[face] += face
        else:
            points[face] = face

    return points

def calculate_sum_points(dice):
    total = 0
    i = 0
    while i < len(dice):
        total += dice[i]
        i += 1
    return total