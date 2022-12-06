def main():
    with open("input.txt") as f:
        lines = f.read()

    window_size = 4  # task 1
    # window_size = 14 # task 2
    pos = 0
    # sliding window
    for i in range(len(lines) - window_size + 1):
        pos += 1
        current_window = lines[i : i + window_size]
        no_repeats = len(set(current_window)) == len(current_window)
        if no_repeats:
            print(f"Found a match! The following packet detected: {current_window}")
            print(
                f"The packet was discovered after the {pos + window_size - 1}th packet"
            )
            break


if __name__ == "__main__":
    main()
