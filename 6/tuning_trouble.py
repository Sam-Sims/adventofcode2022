def main():
    with open("input.txt") as f:
        lines = f.read()

    window_size = 4  # task 1
    # window_size = 14 # task 2
    pos = 0
    # move along lines, taking 4 lines at a time
    for i in range(len(lines) - window_size + 1):
        pos += 1
        current_window = lines[i : i + window_size]
        no_repeats = len(set(current_window)) == len(current_window)
        if no_repeats:
            print("Found a match!")
            print(current_window)
            print(pos + window_size - 1)
            break


if __name__ == "__main__":
    main()
