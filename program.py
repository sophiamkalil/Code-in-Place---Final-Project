# Implementation of the Yacht Dice game
from functions import *

score_card = {
    'simple_rule': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'advanced_rule': {
        'no_combination': -1,
        'four_of_a_kind': -1,
        'full_house': -1,
        'small_straight': -1,
        'large_straight': -1,
        'yahtzee': -1
    }
}

print_score_card(score_card)

round_number = 0
used_combinations = []

while round_number < 12:
    rolled_dice = roll_dice(5)
    stored_dice = []
    rerolls = 0

    print(f'Rolled dice: {rolled_dice}')
    print(f'Stored dice: {stored_dice}')
    print("Enter 1 to store a die, 2 to remove a die, 3 to reroll, 4 to view score card, or 0 to score the round:")

    while True:
        choice = input('>').strip()

        if choice in ['1', '2', '3', '4', '0']:
            if int(choice) == 1:
                print('Enter the index of the die to store (0 to 4):')
                action = int(input('>'))
                result = store_die(rolled_dice, stored_dice, action)
                rolled_dice = result[0]
                stored_dice = result[1]
            elif int(choice) == 2:
                print("Enter the index of the die to remove (0 to 4):")
                action = int(input('>'))
                result = remove_die(rolled_dice, stored_dice, action)
                rolled_dice = result[0]
                stored_dice = result[1]
            elif int(choice) == 3:
                if rerolls < 2:
                    rolled_dice = roll_dice(len(rolled_dice))
                    rerolls += 1
                else:
                    print("You have already used all rerolls.")
            elif int(choice) == 4:
                print_score_card(score_card)
            elif int(choice) == 0:
                valid_combinations = [
                    '1', '2', '3', '4', '5', '6',
                    'no_combination', 'four_of_a_kind',
                    'full_house', 'small_straight',
                    'large_straight', 'yahtzee'
                ]
                print("Enter the desired combination:")
                action = input('>')
                while action not in valid_combinations:
                    print("Invalid combination. Try again.")
                    action = input('>')
                if action not in used_combinations:
                    used_combinations.append(action)
                else:
                    while action in used_combinations:
                        print("This combination has already been used.")
                        action = input('>')
                        while action not in valid_combinations:
                            print("Invalid combination. Try again.")
                            action = input('>')
                    used_combinations.append(action)
                for die in rolled_dice:
                    stored_dice.append(die)
                score_card = make_move(stored_dice, action, score_card)
                rerolls = 0
                round_number += 1
                break

            print(f'Rolled dice: {rolled_dice}')
            print(f'Stored dice: {stored_dice}')
            print("Enter 1 to store a die, 2 to remove a die, 3 to reroll, 4 to view score card, or 0 to score the round:")

        else:
            print("Invalid option. Try again.")

total_score = 0
for points in score_card['simple_rule'].values():
    total_score += points
if total_score >= 63:
    total_score += 35
for points in score_card['advanced_rule'].values():
    total_score += points

print_score_card(score_card)
print(f"Total score: {total_score}")
