stacks = {
    1: "BPNQHDRT",
    2: "WGBJTV",
    3: "NRHDSVMQ",
    4: "PZNMC",
    5: "DZB",
    6: "VCWZ",
    7: "GZNCVQLS",
    8: "LGJMDNV",
    9: "TPMFZCG"
}

def _move_stack(_qty, _from, _to):
    to_move = stacks[_from][-_qty:]
    stacks[_from] = stacks[_from][:-_qty]
    stacks[_to] += to_move

def _print_result():
    result = ""
    for stack in stacks:
        result += stacks[stack][-1:]

    print(result)


with open("input.txt", "r") as input:
    for line in input:
        if line.startswith("move"):
            instructions = line.split(" ")
            _qty = int(instructions[1])
            _from = int(instructions[3])
            _to = int(instructions[5])

            _move_stack(_qty, _from, _to)

_print_result()  # WDLPFNNNB
