from collections import defaultdict


def get_data_from_file(file):
    follow_rules = defaultdict(list)
    updates = []
    filling_rules = True
    file = open(file, "r")
    while True:
        line = file.readline()
        if not line:  # end case
            break

        if filling_rules:
            nums = line.split("|")
            if len(nums) == 1:
                filling_rules = False
                continue
            nums = [x.rstrip() for x in nums]
            nums = [int(x) for x in nums]
            follow_rules[nums[0]].append(nums[1])
        else:
            nums = line.split(",")
            if len(nums) == 1:
                break
            nums = [x.rstrip() for x in nums]
            nums = [int(x) for x in nums]
            updates.append(nums)

    return follow_rules, updates


def check_order(pages, follow_rules):
    for idx in range(len(pages)):
        page = pages[idx]
        following_pages = follow_rules[page]
        for following_page in following_pages:
            prev_pages = pages[0:idx]
            # good if the page is in prev_pages or if it's not present in pages at all
            if following_page in prev_pages:
                # need to now move it right to the next index
                return False
    return True


def check_and_change_order(pages, follow_rules):
    had_to_change = False
    idx = 0
    while True:
        if idx >= len(pages):
            break
        page = pages[idx]
        following_pages = follow_rules[page]
        prev_pages = pages[0:idx]
        to_move = [page for page in prev_pages if page in following_pages]
        prev_pages = [page for page in prev_pages if page not in to_move]
        pages = prev_pages + [pages[idx]] + to_move + pages[idx + 1 :]
        if len(to_move) > 0:
            had_to_change = True
        idx += 1

    return pages if had_to_change else None


def p1():
    # following_rules, updates = get_data_from_file("resources/day5_testinput.txt")
    following_rules, updates = get_data_from_file("resources/day5_input.txt")
    middle_sum = 0
    for update in updates:
        is_in_order = check_order(update, following_rules)
        if is_in_order:
            middle = int((len(update) - 1) / 2)
            middle_sum += update[middle]
    print(middle_sum)


def p2():
    # following_rules, updates = get_data_from_file(
    #     "resources/day5_testinputsmallest.txt"
    # )
    # following_rules, updates = get_data_from_file("resources/day5_testinput.txt")
    following_rules, updates = get_data_from_file("resources/day5_input.txt")
    middle_sum = 0
    for update in updates:
        new_order = check_and_change_order(update, following_rules)
        if new_order is not None:
            middle = int((len(new_order) - 1) / 2)
            middle_sum += new_order[middle]
    print(middle_sum)


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
