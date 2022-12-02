total_points = 0

def _calculate_points(opponent, condition):
    point_map = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    match_map = {
        # first is what is needed to win, then to draw, then to lose
        "A": ["B", "A", "C"],
        "B": ["C", "B", "A"],
        "C": ["A", "C", "B"],
    }

    conditions = ["Z", "Y", "X"]

    # first, find out if we need to win, draw or lose
    match_condition = conditions.index(condition)
    # make a choice based on the condition of the match
    player_choice = match_map[opponent][match_condition]
    # 0 means win, 1 means draw and 2 means loss
    match_points = 6 if match_condition == 0 else 3 if match_condition == 1 else 0 
    choice_points = point_map[player_choice]

    return match_points + choice_points


with open("input.txt", "r") as input:
    for line in input:
        opponent = line[0]
        condition = line[2]
        total_points += _calculate_points(opponent, condition)

print(total_points)  # 11373

