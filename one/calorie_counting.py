

def main():
    with open('input.txt') as f:
        elfs = f.read().split('\n\n')
        total_calories_per_elf = []
        for elf in elfs:
            calories_per_elf = elf.split('\n')

            # convert each item in list to int
            calories_per_elf = list(map(int, calories_per_elf))
            total = sum(calories_per_elf)
            total_calories_per_elf.append(total)

    max_calories = max(total_calories_per_elf)
    print(f"The elf with the highest total calories is {max_calories}")

    total_calories_per_elf.sort()
    total_top_three = sum(total_calories_per_elf[-3:])
    print(f"The top three elves have a total of {total_top_three} calories")

if __name__ == "__main__":
    main()