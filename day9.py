def get_disk_map(file):
    file = open(file, "r")
    line = file.readline()
    chars = [int(char) for char in line]
    return chars


def get_blocks(disk_map):
    is_even = True
    blocks = []
    curr_id = 0
    for num_blocks in disk_map:
        if is_even:
            blocks = blocks + [curr_id for x in range(num_blocks)]
            curr_id += 1
        else:
            blocks = blocks + [None for x in range(num_blocks)]
        is_even = not is_even
    return blocks


class File:
    def __init__(self, id, num_blocks):
        self.id = id
        self.num_blocks = num_blocks


class Space:
    def __init__(self, num_blocks):
        self.num_blocks = num_blocks


def get_files(disk_map):
    files = []
    is_even = True
    curr_id = 0
    for num_blocks in disk_map:
        if is_even:
            files.append(File(curr_id, num_blocks))
            curr_id += 1
        else:
            files.append(Space(num_blocks))
        is_even = not is_even
    only_files = [file for file in files if isinstance(file, File)]
    return files, only_files


def find_file(files, id):
    for i in range(len(files)):
        if isinstance(files[i], File) and files[i].id == id:
            return i


def move_blocks(blocks):
    i = 0
    while i < len(blocks):
        if blocks[i] is None:
            neg_i = -1
            # need to replace with a filled in block
            if blocks[neg_i] is None:
                while (
                    blocks[neg_i] is None and abs(neg_i) < len(blocks) - i
                ):  # make sure we're not searching forever for this
                    neg_i -= 1
            if blocks[neg_i] is not None:
                blocks[i] = blocks[neg_i]
                blocks.pop(neg_i)
            while blocks[-1] is None:
                blocks.pop(-1)

        i += 1

    return blocks


# for each file, find it and then try to move it
def move_files(files, only_files):
    for i in range(len(only_files)):
        file_idx = -1 - i
        file = only_files[file_idx]
        file_location = find_file(files, file.id)
        required_blocks = files[file_location].num_blocks
        # find the leftmost space it'll fit in
        for i in range(0, file_location):
            if isinstance(files[i], Space) and files[i].num_blocks >= required_blocks:
                if files[i].num_blocks == required_blocks:
                    # replace Space with File
                    files[i] = files[file_location]
                else:
                    # need to replace Space with appropriate amount of space
                    files[i].num_blocks = (
                        files[i].num_blocks - files[file_location].num_blocks
                    )
                    files.insert(i, files[file_location])
                    file_location += 1
                files[file_location] = Space(required_blocks)
                break

    return files


def calculate_checksum(blocks):
    sum = 0
    for i in range(len(blocks)):
        if blocks[i] is not None:
            sum += i * blocks[i]
    return sum


def calculate_checksum_from_files(files):
    sum = 0
    i = 0
    runner = []
    for file in files:
        if isinstance(file, File):
            runner.append(file.id)
            num_blocks = file.num_blocks
            for x in range(num_blocks):
                sum += i * file.id
                i += 1
        else:
            runner.append(None)
            for x in range(file.num_blocks):
                i += 1
    return sum


def p1():
    map = get_disk_map("resources/day9_input.txt")
    blocks = get_blocks(map)
    moved_blocks = move_blocks(blocks)
    sum = calculate_checksum(moved_blocks)
    print(sum)
    # 6337367222422


def p2():
    map = get_disk_map("resources/day9_input.txt")
    all, only_files = get_files(map)
    moved_files = move_files(all, only_files)
    sum = calculate_checksum_from_files(moved_files)
    print(sum)
    # 6361380647183


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
