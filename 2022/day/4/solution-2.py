partially_contains = 0

with open("input.txt", "r") as input:
    for line in input:
        pairs = line.strip().split(",")

        first_range = pairs[0][:]
        second_range = pairs[1][:]

        number1 = int(first_range.split("-")[0])
        number2 = int(first_range.split("-")[1])

        number3 = int(second_range.split("-")[0])
        number4 = int(second_range.split("-")[1])

        set1 = set(range(number1, number2+1))
        set2 = set(range(number3, number4+1))

        if set1 & set2:
            partially_contains += 1

print(partially_contains)
