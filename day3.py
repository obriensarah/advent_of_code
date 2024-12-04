import re

def get_data_from_file():
    reports = []
    file = open("resources/day3_input.txt", "r")
    all = file.read()
    return all

def get_pairs(blob):
    regex = "mul\((\d{1}|\d{2}|\d{3}),(\d{1}|\d{2}|\d{3})\)"
    pairs = re.findall(regex,blob)
    pairs = [(int(x), int(y)) for (x,y) in pairs]
    return pairs

def get_pairs_with_switches(blob):
    regex = "mul\((\d{1}|\d{2}|\d{3}),(\d{1}|\d{2}|\d{3})\)|(do\(\))|(don\'t\(\))"
    matches = re.findall(regex, blob)
    pairs_with_switches = [(int(x), int(y)) if x and y else a or b for x,y,a,b in matches]
    return pairs_with_switches 

def multiply_and_add_pairs(pairs):
    sum = 0
    for x, y in pairs:
        sum += x*y
    return sum

def multiply_and_add_pairs_with_switches(pairs_with_switches):
    sum = 0
    switch = 1
    for el in pairs_with_switches:
        if el == "don't()":
            switch = 0
        elif el == "do()":
            switch = 1
        else:
            x,y = el
            if switch:
                sum += x * y
    return sum

def p1(data):
    pairs = get_pairs(data)
    return multiply_and_add_pairs(pairs)

def p2(data):
    pairs_with_switches = get_pairs_with_switches(data)
    return multiply_and_add_pairs_with_switches(pairs_with_switches)

def main():
    # data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    data = get_data_from_file()
    print(p1(data))
    print(p2(data))

if __name__ == "__main__":
    main()