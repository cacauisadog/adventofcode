from collections import defaultdict


elf_to_calories = defaultdict(int)

with open("input.txt", "r") as input:
    elf_counter = 0

    for line in input:
        if line == "\n":
            elf_counter += 1

        else:
            elf_to_calories[elf_counter] += int(line)


sorted_calories = sorted(elf_to_calories.values(), reverse=True)
top_three = sorted_calories[0:3]
print(sum(top_three))  # 207410
