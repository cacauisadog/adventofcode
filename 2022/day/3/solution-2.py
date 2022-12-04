alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def _find_common_item(group):
    s0 = set(group[0])
    s1 = set(group[1])
    s2 = set(group[2])

    # binary magic in the air
    common_item =  s0 & s1 & s2
    return list(common_item)[0]


total_score = 0
current_group = []
with open("input.txt", "r") as input:
    for n, line in enumerate(input):
        current_group.append(line.strip())
        if (n+1)%3 == 0:
            common_item = _find_common_item(current_group)
            item_score = alphabet.index(common_item) + 1
            total_score += item_score
            current_group = []

print(total_score)
