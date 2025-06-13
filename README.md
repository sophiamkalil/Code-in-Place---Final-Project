# 🎲 Yacht Dice Game

A Python implementation of the classic **Yacht Dice** game (similar to Yahtzee), where players roll and store dice, trying to achieve the best combinations and score as high as possible.

## 📦 Project Structure

```plaintext
.
├── funcoes.py      # Contains all core game logic and scoring functions
├── programa.py     # Main script to run the game
└── README.md       # This file
```

## ▶️ How to Play

1. Run the main script:

```bash
python programa.py
```

2. On each turn (12 in total), you:
   - Roll 5 dice.
   - Optionally store or remove dice.
   - Reroll up to 2 times.
   - Choose a scoring category (once per category).
   - Try to maximize your final score.

3. The game ends after all categories are used. The scorecard is displayed along with the total points.

## 📋 Scoring Categories

### Simple Rule:
- Ones (1)
- Twos (2)
- Threes (3)
- Fours (4)
- Fives (5)
- Sixes (6)

### Advanced Rule:
- **no_combination**: sum of all dice
- **four_of_a_kind**: four dice with the same number
- **full_house**: three of a kind + a pair
- **small_straight**: 4-number sequence (e.g. 1-2-3-4)
- **large_straight**: 5-number sequence (e.g. 2-3-4-5-6)
- **yahtzee**: five of a kind (worth 50 points)

🟢 Bonus: If your simple rule total is 63 or more, you get a **+35 point bonus**!

## 🧠 How it Works

- Dice are rolled using Python’s `random.randint`.
- Players choose indices to store/remove dice.
- Score is tracked using dictionaries.
- After 12 rounds, the final score is calculated and printed.

## 📌 Requirements

- Python 3.x
- No external libraries required

## 🖼️ Sample Output

```
Rolled dice: [2, 4, 4, 1, 5]
Stored dice: [4, 4]
Score card:
| 1:             | 01 |
| 2:             |    |
...
Total score: 114
```

## 👤 Author

- [Sophia Kalil]((https://github.com/sophiamkalil))
