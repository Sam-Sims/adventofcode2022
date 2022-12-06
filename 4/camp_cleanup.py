def main():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    split_lines = [line.split(",") for line in lines]

    count = 0
    overlap_count = 0

    for assingment in split_lines:
        elf_1 = assingment[0]
        elf_2 = assingment[1]

        a, b = elf_1.split("-")
        first_range = list(range(int(a), int(b) + 1))
        a, b = elf_2.split("-")
        second_range = list(range(int(a), int(b) + 1))
        # check if any list is a subset of any other list
        if set(first_range).issubset(set(second_range)):
            count += 1
        elif set(second_range).issubset(set(first_range)):
            count += 1

        # check for any overlaps within both lists
        if set(first_range).intersection(set(second_range)):
            overlap_count += 1
        elif set(second_range).intersection(set(first_range)):
            overlap_count += 1

    print(f"There are {count} lists that are subsets of eachother")
    print(f"There are {overlap_count} lists that overlap")


if __name__ == "__main__":
    main()
