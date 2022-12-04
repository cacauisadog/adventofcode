fully_contains = 0

with open("input.txt", "r") as input:
    for line in input:
        pairs = line.strip().split(",")

        first_range = pairs[0][:]
        second_range = pairs[1][:]

        number1 = int(first_range.split("-")[0])
        number2 = int(first_range.split("-")[1])

        number3 = int(second_range.split("-")[0])
        number4 = int(second_range.split("-")[1])

        if (number1 <= number3 and number2 >= number4) or (number3 <= number1 and number4 >= number2):
            fully_contains += 1

print(fully_contains)
