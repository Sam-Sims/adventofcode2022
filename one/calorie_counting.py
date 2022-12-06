

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
            
        print(max(total_calories_per_elf))

if __name__ == "__main__":
    main()