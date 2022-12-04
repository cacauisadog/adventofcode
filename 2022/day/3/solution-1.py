alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def _find_common_items(s1, s2):
    common = []

    for c in s1:
        if c in s2:
            common.append(c)

    # we count by item type, so there can't be any repetitions
    return set(common)


def _get_items_score(common_items):
    score = [alphabet.index(c) + 1 for c in common_items]

    return sum(score)


total_score = 0
with open("input.txt", "r") as input:
    for line in input:
        half = int(len(line)/2)
        first_half = line[0:half]
        second_half = line[half:-1]

        common_items = _find_common_items(first_half, second_half)
        items_score = _get_items_score(common_items)
        total_score += items_score

print(total_score)
