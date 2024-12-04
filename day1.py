def get_lists_from_file():
    ls1 = []
    ls2 = []
    file = open("resources/day1_input.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        splits = line.split(' ')
        val1 = splits[0].rstrip()
        val2 = splits[-1].rstrip()
        ls1.append(int(val1))
        ls2.append(int(val2))

    return ls1, ls2

# sum of differences at each index
def get_distance(ls1, ls2):
    ls1 = sorted(ls1)
    ls2 = sorted(ls2)
    total_diff = 0
    for i in range(len(ls1)): # assumes list lengths are equal
        diff = abs(ls1[i] - ls2[i])
        # print("distance between", ls1[i],"and", ls2[i], "is", diff)
        total_diff += diff

    return total_diff

def get_similarity(ls1, ls2):
    ls1 = sorted(ls1)
    ls2 = sorted(ls2)
    total_sim = 0
    for val in ls1:
        # could traverse sorted list to find value for performance but to brute force it:
        matching_values = [el for el in ls2 if el == val]
        num_matches = len(matching_values)
        sim_score = val * num_matches
        total_sim += sim_score

    return total_sim

def main():
    ls1, ls2 = get_lists_from_file()
    # ls1 = [3,4,2,1,3,3]
    # ls2 = [4,3,5,3,9,3]
    # distance = get_distance(ls1, ls2)
    sim = get_similarity(ls1, ls2)
    print(sim)

if __name__=="__main__":
    main()