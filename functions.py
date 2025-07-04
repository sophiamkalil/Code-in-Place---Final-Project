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

def calculate_small_straight_points(dice):
    sequences = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    for seq in sequences:
        all_present = True
        for num in seq:
            if num not in dice:
                all_present = False
                break
        if all_present:
            return 15
    return 0

def calculate_large_straight_points(dice):
    sequences = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]
    for seq in sequences:
        all_present = True
        for num in seq:
            if num not in dice:
                all_present = False
                break
        if all_present:
            return 30
    return 0

def calculate_full_house_points(dice_faces):
    total = sum(dice_faces)

    first_value = dice_faces[0]
    count_first = dice_faces.count(first_value)

    if count_first == 3:
        second_value = None
        for face in dice_faces:
            if face != first_value:
                second_value = face
                break
        if second_value is not None and dice_faces.count(second_value) == 2:
            return total

    elif count_first == 2:
        second_value = None
        for face in dice_faces:
            if face != first_value:
                second_value = face
                break
        if second_value is not None and dice_faces.count(second_value) == 3:
            return total

    return 0

def calculate_four_of_a_kind_points(dice_faces):
    total = sum(dice_faces)

    frequencies = {}
    for face in dice_faces:
        if face not in frequencies:
            frequencies[face] = 1
        else:
            frequencies[face] += 1

    for count in frequencies.values():
        if count >= 4:
            return total

    return 0

def calculate_yahtzee_points(dice):
    if len(dice) < 5:
        return 0
    for num in dice:
        if dice.count(num) >= 5:
            return 50
    return 0

def calculate_advanced_rule_points(dice):
    return {
        'yahtzee': calculate_yahtzee_points(dice),
        'full_house': calculate_full_house_points(dice),
        'four_of_a_kind': calculate_four_of_a_kind_points(dice),
        'no_combination': calculate_sum_points(dice),
        'large_straight': calculate_large_straight_points(dice),
        'small_straight': calculate_small_straight_points(dice)
    }

def make_move(dice_list, category, score_card):
    advanced = calculate_advanced_rule_points(dice_list)
    simple = calculate_simple_rule_points(dice_list)

    if category in advanced:
        score_card['advanced_rule'][category] = advanced[category]
    else:
        try:
            category_num = int(category)
            if category_num in simple:
                score_card['simple_rule'][category_num] = simple[category_num]
        except ValueError:
            pass

    return score_card

def print_score_card(score_card):
    print("Score Card:")
    print("-" * 25)
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if score_card['simple_rule'][i] != -1:
            print(f"| {i}: {filler}| {score_card['simple_rule'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for key in score_card['advanced_rule'].keys():
        filler = " " * (15 - len(str(key)))
        if score_card['advanced_rule'][key] != -1:
            print(f"| {key}: {filler}| {score_card['advanced_rule'][key]:02} |")
        else:
            print(f"| {key}: {filler}|    |")
    print("-" * 25)