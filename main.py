from dice_calculator import dice_calculator
from api_handler import spell_requester
from math import sqrt


class Result:
    def __init__(self, result_id, og_inc, min_inc, max_inc, mean_inc):
        self.result_id = result_id
        self.og_dice_input = og_inc
        self.global_min = min_inc
        self.global_max = max_inc
        self.global_mean = mean_inc
        self.variance = sqrt((self.global_max - self.global_min) ** 2) + 1

    def display(self):
        input(f"""
- - - - - Evaluation - - - - -
Result ID: {self.result_id}
Input: {self.og_dice_input}

Mean of the dice roll: {self.global_mean}
Minimum outcome: {self.global_min}
Maximum outcome: {self.global_max}
Variance: {self.variance}

Press Enter to continue.
        """)


results = []
while True:
    response = input(
        "Please choose input type!\nStandard Dice Notation: 1\nSpell evaluation: 2\nLoad: 3\nExit: e\n"
    )

    match response:
        case "e":
            break
        case "1":  # standard dice notation
            og_dice_input = input("Please input generic dice notation. (like 2d20 or 1d4+2)\n")
            g_max, g_min, g_mean = dice_calculator(og_dice_input)
            results.append(Result(len(results), og_dice_input, g_max, g_min, g_mean))
            results[-1].display()
        case "2":  # spell evaluation
            og_spell_input = input("Please input a DnD 5e SRD spell's full name.\n")
            og_dice_input = spell_requester(og_spell_input)
            g_max, g_min, g_mean = dice_calculator(og_dice_input)
            results.append(Result(len(results), f"{og_spell_input} ({og_dice_input})", g_max, g_min, g_mean))
            results[-1].display()
        case "3":  # load
            result_to_display = int(input("Please enter the Result ID of the result you want displayed\n"))
            results[result_to_display].display()
        case _:
            print("Please give a valid input.\n")

pass
