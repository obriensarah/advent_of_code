from collections import defaultdict

def get_lists_from_file():
    lines = []
    file = open("resources/day4_input.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line.rstrip())

    return lines

class XMASSearch:
    def __init__(self):
        self.lines = get_lists_from_file()
        # self.lines = [
        #     "MMMSXXMASM", 
        #     "MSAMXMSMSA", 
        #     "AMXSXMAAMM", 
        #     "MSAMASMSMX", 
        #     "XMASAMXAMM", 
        #     "XXAMMXXAMA", 
        #     "SMSMSASXSS", 
        #     "SAXAMASAAA", 
        #     "MAMMMXMMMM", 
        #     "MXMXAXMASX"
        # ]
        self.word_len = len('xmas')
        self.x_len = len(self.lines[0])
        self.y_len = len(self.lines)
        self.search_funcs = [
            (self._search_l_to_r, 'lr'), 
            (self._search_r_to_l, 'rl'),
            (self._search_down, 'd'),
            (self._search_up, 'u'), 
            (self._search_down_left, 'dl'),
            (self._search_down_right, 'dr'),
            (self._search_up_left, 'ul'),
            (self._search_up_right, 'ur')
        ]

    def search(self):
        positive_searches = [] # starting coordinates with direction
        for y in range(self.y_len):
            for x in range(self.x_len):
                for func in self.search_funcs:
                    result = func[0](x,y)
                    if result:
                        positive_searches.append((x,y, func[1]))
        return positive_searches

    def _search_l_to_r(self, x, y):
        """start (x,y), search left to right"""
        if y < self.y_len and x <= self.x_len - self.word_len:
            for i in range(self.word_len):
                letter = self.lines[y][x + i]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds

    def _search_r_to_l(self, x, y):
        """start (x,y), search right to left"""
        if y < self.y_len and x >= self.word_len - 1:
            for i in range(self.word_len):
                letter = self.lines[y][x - i]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds

    def _search_down(self, x, y):
        """start (x,y), search down"""
        if y <= self.y_len - self.word_len and x < self.x_len:
            for i in range(self.word_len):
                letter = self.lines[y + i][x]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds

    def _search_up(self, x, y):
        """start (x,y), search up"""
        if y >= self.word_len - 1 and x < self.x_len:
            for i in range(self.word_len):
                letter = self.lines[y - i][x]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds

    def _search_up_right(self, x, y):
        """start (x,y), search up and right"""
        if y >= self.word_len - 1 and x <= self.x_len - self.word_len:
            for i in range(self.word_len):
                letter = self.lines[y - i][x + i]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds

    def _search_up_left(self, x, y):
        """start (x,y), search up and left"""
        if y >= self.word_len - 1 and x >= self.word_len - 1:
            for i in range(self.word_len):
                letter = self.lines[y - i][x - i]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds


    def _search_down_left(self, x, y):
        """start (x,y), search down and left"""
        if y <= self.y_len - self.word_len and x >= self.word_len - 1:
            for i in range(self.word_len):
                letter = self.lines[y + i][x - i]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds

    def _search_down_right(self, x, y):
        """start (x,y), search down and left"""
        if y <= self.y_len - self.word_len and x <= self.x_len - self.word_len:
            for i in range(self.word_len):
                letter = self.lines[y + i][x + i]
                if i == 0 and letter.lower() != "x":
                    return False 
                elif i == 1 and letter.lower() != "m":
                    return False
                elif i == 2 and letter.lower() != "a":
                    return False
                elif i == 3 and letter.lower() != "s":
                    return False
            return True
        else:
            return False # out of bounds


class MASMASSearch:
    def __init__(self):
        self.lines = get_lists_from_file()
        # self.lines = [
        #     "MMMSXXMASM", 
        #     "MSAMXMSMSA", 
        #     "AMXSXMAAMM", 
        #     "MSAMASMSMX", 
        #     "XMASAMXAMM", 
        #     "XXAMMXXAMA", 
        #     "SMSMSASXSS", 
        #     "SAXAMASAAA", 
        #     "MAMMMXMMMM", 
        #     "MXMXAXMASX"
        # ]
        self.x_len = len(self.lines[0])
        self.y_len = len(self.lines)
        self.search_funcs = [
            (self._search_lr, 'lr'), 
            (self._search_du, 'du'),
            (self._search_dl, 'dl'),
            (self._search_dr, 'dr')
        ]

    def search(self):
        positive_searches = [] # starting coordinates
        for y in range(1, self.y_len - 1):
            for x in range(1, self.x_len - 1):
                # if self._search_lr(x,y) and self._search_du(x,y):
                #     positive_searches.append((x,y))
                if self._search_dl(x,y) and self._search_dr(x,y):
                    positive_searches.append((x,y))
        return positive_searches

    def _search_lr(self, x, y):
        """middle (x,y), oriented left to right"""
        found_letters = ""
        for i in [-1, 0, 1]:
            letter = self.lines[y][x + i].lower()
            found_letters += letter
            if i == 0 and letter.lower() != "a":
                return False
            elif (i == 1 or i == -1) and letter != "m" and letter != "s":
                return False
        if found_letters == "mas" or found_letters == "sam":
            return True
        else:
            return False

    def _search_du(self, x, y):
        """middle (x,y), oriented up and down"""
        found_letters = ""
        for i in [-1, 0, 1]:
            letter = self.lines[y + i][x].lower()
            found_letters += letter
            if i == 0 and letter.lower() != "a":
                return False
            elif (i == 1 or i == -1) and letter != "m" and letter != "s":
                return False
        if found_letters == "mas" or found_letters == "sam":
            return True
        else:
            return False

    def _search_dl(self, x, y):
        """middle (x,y), oriented slope up"""
        found_letters = ""
        for i in [-1, 0, 1]:
            letter = self.lines[y + i][x - i].lower()
            found_letters += letter
            if i == 0 and letter.lower() != "a":
                return False
            elif (i == 1 or i == -1) and letter != "m" and letter != "s":
                return False
        if found_letters == "mas" or found_letters == "sam":
            return True
        else:
            return False

    def _search_dr(self, x, y):
        """middle (x,y), oriented slope down"""
        found_letters = ""
        for i in [-1, 0, 1]:
            letter = self.lines[y + i][x + i].lower()
            found_letters += letter
            if i == 0 and letter.lower() != "a":
                return False
            elif (i == 1 or i == -1) and letter != "m" and letter != "s":
                return False
        if found_letters == "mas" or found_letters == "sam":
            return True
        else:
            return False


def p1():
    s = XMASSearch()
    print(len(s.search()))

def p2():
    s = MASMASSearch()
    print(len(s.search()))

if __name__ == "__main__":
    p1()
    p2()

