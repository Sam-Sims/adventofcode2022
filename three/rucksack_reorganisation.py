def get_priority(item):
    # use ascii encoding to get the priority
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96


def main():
    # Read the input.txt
    priority_list = []
    with open("input.txt", "r") as f:
        items = f.read().splitlines()

    for item in items:
        item.strip()
        half = int(len(item) / 2)
        print(f"Input string: {item}")

        first_half = item[:half]
        second_half = item[half:]
        print(f"Splitting into two halves: {first_half} and {second_half}")
        seen_list = []
        for item in first_half:
            if item in second_half:
                if item not in seen_list:
                    print(
                        f"Found a match: {item}. The priority is {get_priority(item)}. Adding {item} to the seen list."
                    )
                    priority_list.append(get_priority(item))
                    seen_list.append(item)

    chunked_priority_list = []
    # chunk the list into chunks of 3 in a list
    chunked_list = [items[i : i + 3] for i in range(0, len(items), 3)]
    for chunk in chunked_list:
        common = set.intersection(*map(set, chunk))
        common = str(common)[
            2  # hacky way to get the character in the set - assuming only 1 character will be always be returned
        ]
        chunked_priority_list.append(get_priority(common))

    print(sum(priority_list))
    print(sum(chunked_priority_list))


if __name__ == "__main__":
    main()
