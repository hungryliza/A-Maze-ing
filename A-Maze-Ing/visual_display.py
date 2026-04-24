# from mazegen import MazeGenerator
# import sys
# import random


class Compass:
    def __init__(self, cellval):
        self.north = cellval & 1 == 1
        self.east = cellval & 2 == 2
        self.south = cellval & 4 == 4
        self.west = cellval & 8 == 8
        self.cellval = cellval


class Display:
    def __init__(self, maze, path=None, show=False):
        self.maze = maze
        self.path = path if path else []
        self.show = show
        self.color = {"white": "47",
                      "blue": "44"}

    def render(self):
        for maze_y in range(self.maze.height):
            for maze_x in range(self.maze.width):
                cellval = self.maze.basegrid.cells[maze_y][maze_x]
                direction = Compass(cellval)
                print("+", end="")
                if maze_y == 0 or direction.north \
                or (maze_x, maze_y) in self.maze.fortytwo \
                or (maze_x, maze_y - 1) in self.maze.fortytwo:
                    print("───", end="")
                else:
                    print("   ", end="")
            print("+")

            for maze_x in range(self.maze.width):
                cellval = self.maze.basegrid.cells[maze_y][maze_x]
                direction = Compass(cellval)
                if maze_x == 0 or direction.west \
                or (maze_x, maze_y) in self.maze.fortytwo \
                or (maze_x - 1, maze_y) in self.maze.fortytwo:
                    print("|", end="")
                else:
                    print(" ", end="")
                pos = (maze_x, maze_y)
                current_posyx = (maze_y, maze_x)
                if pos in self.maze.fortytwo:
                    print(" ✹ ", end="")
                elif current_posyx == self.maze.entry:
                    print(" ▶ ", end="")
                elif current_posyx == self.maze.exit:
                    print(" ⚑ ", end="")
                elif self.show and pos in self.path:
                    print(" ▹ ", end="")
                else:
                    print("   ", end="")
            print("|")
        for maze_x in range(self.maze.width):
            cellval = self.maze.basegrid.cells[maze_y][maze_x]
            direction = Compass(cellval) 
            print("+", end="")
            print("───", end="")
        print("+")


# if __name__ == "__main__":
#     gen = MazeGenerator(
#         width=10, height=10,
#         entry=(0, 0), exit=(9, 9),
#         perfect=True, seed=42
#     )
#     gen.generate()
#     display = Display(gen)
#     seed = 1
#     while True:
#         display.render()
#         print("=== A-Maze-ing ===")
#         print("1. Re-generate a new maze")
#         print("2. Show/Hide path from entry to exit")
#         print("3. Rotate maze colors")
#         print("4. Quit")
#         choice = input("Choice? (1-4): ")
#         if choice == "1":
#             seed += 1
#             gen.seed = seed
#             random.seed(seed)
#             gen.generate()
#         elif choice == "2":
#             if display.show is False:
#                 display.show = True
#             else:
#                 display.show = False
#         elif choice == "3":
#             display.color = "blue"
#         elif choice == "4":
#             sys.exit(0)
