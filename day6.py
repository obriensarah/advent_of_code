import copy 

def get_lists_from_file(file):
    lines = []
    file = open(file, "r")
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line.rstrip())

    return lines

class Guard:
    def __init__(self, lab):
        self.lab = lab
        self.x_len = len(lab[0])
        self.y_len = len(lab)
        self.directions = ['up', 'right', 'down', 'left']
        self.curr_direction = 0 # corresponding to indices in above^
        self.coords = self.find_guard()
        self.visited_positions = {self.coords}
    
    def turn(self):
        self.curr_direction = (self.curr_direction + 1) % 4

    def find_guard(self):
        for row_num in range(self.y_len):
            for col_num in range(self.x_len):
                if self.lab[row_num][col_num] == "^":
                    return (col_num, row_num)

    def walk(self):
        while True: 
            if not self.is_in_bounds(self.coords):
                # stepped out of bounds
                break

            _ = self.step()

        return len(self.visited_positions)

    def is_in_bounds(self, coords):
        if coords[0] < 0 or coords[1] < 0 or coords[0] >= self.x_len or coords[1] >= self.y_len:
            return False
        return True
            
    def step(self):
        temp_coords = self.coords
        if self.curr_direction == 0: # up
            temp_coords = (self.coords[0], self.coords[1] - 1)
        elif self.curr_direction == 1: # right
            temp_coords = (self.coords[0] + 1, self.coords[1])
        elif self.curr_direction == 2: # down
            temp_coords = (self.coords[0], self.coords[1] + 1)
        elif self.curr_direction == 3: # left
            temp_coords = (self.coords[0] - 1, self.coords[1])
        
        x, y = temp_coords
        is_in_bounds = self.is_in_bounds(temp_coords)
        if is_in_bounds and self.lab[y][x] == "#":
            # we've hit an obstacle. turn and step again.
            self.turn()
            self.step()
            return

        self.coords = temp_coords
        if is_in_bounds:
            self.visited_positions.add(temp_coords)
        
        return


class LoopyGuard:
    def __init__(self, lab):
        self.lab = lab
        self.x_len = len(lab[0])
        self.y_len = len(lab)
        self.directions = ['up', 'right', 'down', 'left']
        self.curr_direction = 0 # corresponding to indices in above^
        self.coords = self.find_guard()
        self.visited_positions = {self.coords}
    
    def turn(self):
        self.curr_direction = (self.curr_direction + 1) % 4

    def find_guard(self):
        for row_num in range(self.y_len):
            for col_num in range(self.x_len):
                if self.lab[row_num][col_num] == "^":
                    return (col_num, row_num)    

    def walk(self):
        has_loop = False
        while not has_loop: 
            if not self.is_in_bounds(self.coords):
                # stepped out of bounds
                break

        return self.step()

    def is_in_bounds(self, coords):
        if coords[0] < 0 or coords[1] < 0 or coords[0] >= self.x_len or coords[1] >= self.y_len:
            return False
        return True
            
    def step(self):
        temp_coords = self.coords
        if self.curr_direction == 0: # up
            temp_coords = (self.coords[0], self.coords[1] - 1)
        elif self.curr_direction == 1: # right
            temp_coords = (self.coords[0] + 1, self.coords[1])
        elif self.curr_direction == 2: # down
            temp_coords = (self.coords[0], self.coords[1] + 1)
        elif self.curr_direction == 3: # left
            temp_coords = (self.coords[0] - 1, self.coords[1])
        
        x, y = temp_coords
        is_in_bounds = self.is_in_bounds(temp_coords)
        if is_in_bounds and self.lab[y][x] == "#":
            # we've hit an obstacle. turn and step again.
            self.turn()
            is_loop = self.step()
            return is_loop

        self.coords = temp_coords
        if is_in_bounds:
            # check if already there, check which direction we were going
            if (temp_coords, self.curr_direction) in self.visited_positions:
                # already was here - return True
                return True
            self.visited_positions.add((temp_coords, self.curr_direction))
        
        return
 
def p2():
    # lab = get_lists_from_file("resources/day6_testinput.txt")
    lab = get_lists_from_file("resources/day6_input.txt")
    x_len = len(lab[0])
    y_len = len(lab)
    loops = 0
    for x in range(x_len):
        for y in range(y_len):
            print("inside", x, y)
            if lab[y][x] != ".":
                continue
            temp_lab = copy.copy(lab)
            row = temp_lab[y]
            temp_lab[y] = row[:x] + "#" + row[x+1:]
            g = LoopyGuard(temp_lab)
            has_loop = g.walk()
            if has_loop:
                loops += 1
    print("loops", loops)

def p1():
    # lab = get_lists_from_file("resources/day6_testinput.txt")
    lab = get_lists_from_file("resources/day6_input.txt")
    g = Guard(lab)
    print(g.walk())

def main():
    p1()
    p2()

if __name__ == "__main__":
    main()