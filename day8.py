from collections import defaultdict


def get_lists_from_file(file):
    lines = []
    file = open(file, "r")
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line.rstrip())

    return lines


def get_nodes_by_frequency(field):
    nodes = defaultdict(list)
    for row_idx in range(len(field)):
        for col_idx in range(len(field[0])):
            frequency = field[col_idx][row_idx]
            if frequency != ".":
                nodes[frequency].append((col_idx, row_idx))
    return nodes


def get_pairs(nodes):
    """gets all possible pairs of nodes in the list"""
    pairs = set()
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            pairs.add((nodes[i], nodes[j]))
    return pairs


def get_distance(pair):
    node_ax, node_ay = pair[0]
    node_bx, node_by = pair[1]
    return (node_ax - node_bx, node_ay - node_by)


def get_antinodes_specified_distance(pair):
    distx, disty = get_distance(pair)
    # node a plus distance, node b minus distance
    node_ax, node_ay = pair[0]
    node_bx, node_by = pair[1]
    an1 = (node_ax + distx, node_ay + disty)
    an2 = (node_bx - distx, node_by - disty)
    return an1, an2


def get_antinodes(pair, x_len, y_len):
    distx, disty = get_distance(pair)
    # node a plus distance, node b minus distance
    node_ax, node_ay = pair[0]
    node_bx, node_by = pair[1]
    antinodes = set()
    # first add the originals
    antinodes.add(pair[0])
    antinodes.add(pair[1])
    # get all in-bounds in line
    an1 = (node_ax + distx, node_ay + disty)
    while check_in_bounds(an1, x_len, y_len):
        antinodes.add(an1)
        an1 = (an1[0] + distx, an1[1] + disty)
    an2 = (node_bx - distx, node_by - disty)
    while check_in_bounds(an2, x_len, y_len):
        antinodes.add(an2)
        an2 = (an2[0] - distx, an2[1] - disty)
    return antinodes


def check_in_bounds(node, x_len, y_len):
    return node[0] >= 0 and node[1] >= 0 and node[0] < x_len and node[1] < y_len


def p1():
    field = get_lists_from_file("resources/day8_input.txt")
    nodes_by_frequency = get_nodes_by_frequency(field)
    x_len = len(field[0])
    y_len = len(field)
    antinodes = set()
    for nodes in nodes_by_frequency.values():
        pairs = get_pairs(nodes)
        for pair in pairs:
            an1, an2 = get_antinodes_specified_distance(pair)
            if check_in_bounds(an1, x_len, y_len):
                antinodes.add(an1)
            if check_in_bounds(an2, x_len, y_len):
                antinodes.add(an2)
    print(len(antinodes))


def p2():
    field = get_lists_from_file("resources/day8_input.txt")
    nodes_by_frequency = get_nodes_by_frequency(field)
    x_len = len(field[0])
    y_len = len(field)
    antinodes = set()
    for nodes in nodes_by_frequency.values():
        pairs = get_pairs(nodes)
        for pair in pairs:
            an = get_antinodes(pair, x_len, y_len)
            antinodes = antinodes.union(an)
    print(len(antinodes))


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()
