total_points = 0

def _calculate_points(opponent, player):
    point_map = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    match_map = {
        # first is what is needed to win, then to draw, then to lose
        "A": ["Y", "X", "Z"],
        "B": ["Z", "Y", "X"],
        "C": ["X", "Z", "Y"],
    }

    match_outcome = match_map[opponent].index(player)
    # 0 means win, 1 means draw and 2 means loss
    match_points = 6 if match_outcome == 0 else 3 if match_outcome == 1 else 0 
    choice_points = point_map[player]

    return match_points + choice_points


with open("input.txt", "r") as input:
    for line in input:
        opponent = line[0]
        player = line[2]
        total_points += _calculate_points(opponent, player)

print(total_points)  # 13005
