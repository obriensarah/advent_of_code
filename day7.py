class Equation:
    def __init__(self, equation):
        splits = equation.split(" ")
        self.test_value = int(splits[0].replace(":", ""))
        self.members = [int(x) for x in splits[1:]]
        return


def get_equations_from_file(file):
    equations = []
    file = open(file, "r")
    while True:
        line = file.readline()
        if not line:
            break
        equations.append(Equation(line.rstrip()))

    return equations


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


def get_perms(num_spaces, operators=[add, mul]):
    if num_spaces == 1:
        return [[operator] for operator in operators]

    options = []
    prev_letter_options = get_perms(num_spaces - 1, operators)
    for option in prev_letter_options:
        for operator in operators:
            options.append(option + [operator])
    return options


def do_math(members, operations):
    """perform all operations on members"""
    if len(members) == 2:
        return operations[0](members[0], members[1])

    return operations[-1](do_math(members[:-1], operations[:-1]), members[-1])


def get_sum_of_feasible_equations(operators=[add, mul]):
    equations = get_equations_from_file("resources/day7_input.txt")
    # for each equation, try all permutations
    results_sum = 0
    for equation in equations:
        perms = perms = get_perms(
            len(equation.members) - 1, operators
        )  # 2^len(equation.members)-1
        for perm in perms:
            result = do_math(equation.members, perm)
            if result == equation.test_value:
                results_sum += result
                break

    print(results_sum)


def p1():
    get_sum_of_feasible_equations()


def p2():
    get_sum_of_feasible_equations([add, mul, concat])


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
