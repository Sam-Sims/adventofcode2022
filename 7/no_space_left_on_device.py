from pathlib import Path


def build_filesystem(lines):
    current_dir = Path("")
    filesystem_structure = {}

    for line in lines:
        line.strip()
        split_line = line.split()
        # if the first element is a number, convert it to an int to check in the case statement (starts with num = file)
        if split_line[0].isdigit():
            split_line[0] = int(split_line[0])

        match split_line:
            case "$", "cd", "..":
                # We are moving up a directory
                print("Moving up a directory")
                current_dir = current_dir.parent
            case "$", "cd", *args:
                # We are moving to a target directory
                print("Moving to a target directory")
                name = args[0]
                print(f"Directory name: {name}")
                current_dir = current_dir / name
                print(f"Current directory: {current_dir}")
                filesystem_structure[current_dir] = []
            case "dir", *args:
                # The path must be at the current level
                dirname = args[0]
                print(f"Child directory: {dirname}")
                filesystem_structure[current_dir].append(current_dir / dirname)
            case int(), *args:
                # Begins with number so must be a file
                filename = args[0]
                print(f"Child file: {filename}")
                filesystem_structure[current_dir].append((filename, split_line[0]))
    # print(filesystem_structure)
    return filesystem_structure


def calc_dir_size(key, filesystem_structure):
    """Recursively calculate the size of a directory"""
    total_size = 0
    # loop through each child which can either be a file or a directory
    for child in filesystem_structure[key]:
        # if the child is a tuple, it is a file as it contains a size and a filename
        if isinstance(child, tuple):
            # Add the filesize to the total size of the directory
            total_size += child[1]
        else:
            # If it is a directory then recursively call this function to calculate the size of the next directory
            total_size += calc_dir_size(child, filesystem_structure)
    # return the total size of the directory and all subdirectories
    return total_size


def calc_file_sizes(filesystem_structure, limit):
    total_size = 0
    dir_sizes = {}
    # loop through each file path in the dictionary
    for dir in filesystem_structure.keys():
        print(dir)
        #  recursively calculate the size of the directory
        dir_size = calc_dir_size(dir, filesystem_structure)
        # store the size of the directory in a dictionary
        dir_sizes[dir] = dir_size
        # if the size of the directory is under the limit, add it to the total size
        if dir_size < limit:
            print(f"Directory {dir} is under the limit")
            total_size += dir_size
    print(total_size)


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        lines
    fs_structure = build_filesystem(lines)
    calc_file_sizes(fs_structure, 100000)


if __name__ == "__main__":
    main()
