import random

class MazeGrid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = [[15 for col in range(self.width)]for row in range(self.height)]


class MazeGenerator:
    def __init__(self, width, height, entry, exit, perfect=True, seed=0):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        random.seed(self.seed)
        self.basegrid = MazeGrid(self.height, self.width)
        self.fortytwo = []


    def generate(self):
        self.basegrid = MazeGrid(self.height, self.width)
        self.pattern()
        start_y, start_x = self.entry
        height = self.height
        width = self.width
        rando = random.Random(self.seed)
        exit_x, exit_y = self.exit

        stack = [(start_x, start_y)]
        visited = {(start_x, start_y)}

        directions = [
            (0, -1, 1, 4),
            (1, 0, 2, 8),
            (0, 1, 4, 1),
            (-1, 0, 8, 2)
        ]
        while stack:
            curr_x, curr_y = stack[-1]
            unvisited_walls = []
            for dx, dy, wall_curr, wall_next in directions:
                nx, ny = curr_x + dx, curr_y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited and (nx, ny) not in self.fortytwo:
                    unvisited_walls.append((nx, ny, wall_curr, wall_next))
            if unvisited_walls:
                nx, ny, wall_curr, wall_next = rando.choice(unvisited_walls)
                self.basegrid.cells[curr_y][curr_x] -= wall_curr
                self.basegrid.cells[ny][nx] -= wall_next
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()
        if self.perfect is False:
            rx = rando.randint(0, width - 2)
            ry = rando.randint(0, height - 1)
            if self.basegrid.cells[ry][rx] & 2:
                self.basegrid.cells[ry][rx] -= 2
                self.basegrid.cells[ry][rx + 1] -= 8
        return self.basegrid.cells


    def pattern(self):
        if self.height >= 7 and self.width >= 9:
            fortytwopattern = [(0,0),(0,1),(0,2),(1,2),(2,2),(2,3),(2,4),(4,0),
                        (5,0),(6,0),(6,1),(4,2),(5,2),(6,2),(4,3),(4,4),(5,4),(6,4)]
            placed = []
            placex = int((self.width - 7) / 2)
            placey = int((self.height - 5) / 2)
            for (i,j) in fortytwopattern:
                placed.append((i + placex, j + placey))
            self.fortytwo = placed
            for (x, y) in self.fortytwo:
                self.basegrid.cells[y][x] = 16
        else:
            print("Maze too small to print 42 pattern")
            # gridtoosmall = input("Do you still want to print grid ? ")
            # if gridtoosmall == "yes":
            #     print(self.basegrid.cells)
            # else:
            #     sys.exit(1)


# if __name__ == "__main__":
#     gen = MazeGenerator(
#         width=20, height=20,
#         entry=(0,0), exit=(19,19),
#         perfect=True, seed=42
#     )
#     gen.generate()
#     for row in gen.basegrid.cells:
#         print(f"{row}")
#         # for cell in row:
#         #     if cell == 16:
#         #         print("#", end=" ")
#         #     else:
#         #         print(".", end=" ")
#         # print()
