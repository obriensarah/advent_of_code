import copy 
def get_lists_from_file():
    reports = []
    file = open("resources/day2_input.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        splits = line.split(' ')
        reports.append([int(split.rstrip()) for split in splits])

    return reports

def is_report_safe(report):
    increasing = None
    for idx in range(len(report)):
        if idx > 0:
            diff = report[idx] - report[idx-1]
            inc = diff > 0
            if increasing is not None and inc != increasing:
                return False
            if abs(diff) < 1 or abs(diff) > 3:
                return False
            increasing = inc
    return True

def could_report_be_safe(report):
    is_safe = is_report_safe(report)
    if is_safe:
        return True
    if not is_safe:
        for idx in range(len(report)):
            new_report = copy.copy(report)
            new_report.pop(idx)
            is_safe = is_report_safe(new_report)
            if is_safe: 
                return True
    return False        

def main():
    reports = get_lists_from_file()
    # reports = [
    #     [7, 6, 4, 2, 1],
    #     [1, 2, 7, 8, 9],
    #     [1, 3, 2, 4, 5]
    # ]
    safe_counter = 0
    for report in reports:
        # is_safe = is_report_safe(report)
        is_safe = could_report_be_safe(report)
        if is_safe:
            safe_counter += 1
    print(safe_counter)

if __name__ == "__main__":
    main()