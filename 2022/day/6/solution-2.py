unique_chars = ""
char_count = 0

with open("input.txt", "r") as input:
    line = input.readline().strip()

    for n, char in enumerate(line):
        if char in unique_chars:
            pos = unique_chars.index(char)
            unique_chars = unique_chars[pos+1::]
            
        unique_chars += char
        if len(unique_chars) == 14:
            char_count = n + 1
            break

print(char_count)  # 2250
