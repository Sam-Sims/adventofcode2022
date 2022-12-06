def construct_stacks(stack):
    stacks = []
    for row in stack:
        parsed_row = row[1:-1:4]
        for i in range(len(parsed_row)):
            if len(stacks) < i + 1:
                stacks.append([])
            if parsed_row[i] != " ":
                stacks[i].append(parsed_row[i])
    for crate in stacks:
        crate.reverse()
    return stacks


def parse_instructions(instructions):
    instruction_list = []
    for instruction in instructions:
        _, count, _, source, _, dest = instruction.split()
        instruction = [int(count), int(source), int(dest)]
        instruction_list.append(list(instruction))
    return instruction_list


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    stacks = construct_stacks(lines[0:8])
    instructions = lines[10:]
    instructions = parse_instructions(instructions)
    for count, source, dest in instructions:
        for i in range(count):
            stacks[dest - 1].append(stacks[source - 1].pop())

    for stack in stacks:
        print(stack)


if __name__ == "__main__":
    main()
