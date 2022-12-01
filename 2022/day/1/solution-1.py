most_calories = 0
calories = 0

with open("input.txt", "r") as input:
    for line in input:
        if line == "\n":
            if calories > most_calories:
                most_calories = calories
            calories = 0

        else:
            calories += int(line)

# I need to check again if calories > most_calories,
# since the context manager automatically closes
# the file when the lines end
print(max(calories, most_calories))  # 72602
