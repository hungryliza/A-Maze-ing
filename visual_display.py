from mazegen import MazeGenerator
import sys
import random

class Compass:
    def __init__(self, cellval):
        self.north = cellval & 1 == 1
        self.east = cellval & 2 == 2
        self.south = cellval & 4 == 4
        self.west = cellval & 8 == 8
        self.cellval = cellval


class Display:
    def __init__(self, maze, show=False, color="white", path=None):
        self.maze = maze
        self.path = path
        self.show = show
        self.color = color


    def render(self):
        # gridwidth = 2 * self.maze.width + 1
        # gridheight = 2 * self.maze.height + 1
        # grid = [[" " for col in range(gridwidth)] for row in range(gridheight)]
        # for maze_y in range(self.maze.height):
        #     for maze_x in range(self.maze.width):
        #         cellval = self.maze.basegrid.cells[maze_y][maze_x]
        #         direction = Compass(cellval)
        #         if direction.north:
        #             grid[2*maze_y][2*maze_x+1] = "─"
        #         if direction.west:
        #             grid[2*maze_y+1][2*maze_x] = "|"
        #         if direction.south:
        #             grid[2*maze_y+2][2*maze_x+1] = "─"
        #         if direction.east:
        #             grid[2*maze_y+1][2*maze_x+2] = "|"
        #         grid[2*maze_y][2*maze_x] = "+"
        #         grid[2*maze_y][2*self.maze.width] = "+"
        #         if (maze_x, maze_y) == self.maze.entry:
        #             grid[2*maze_y+1][2*maze_x+1] = "▶"
        #         elif (maze_x, maze_y) == self.maze.exit:
        #             grid[2*maze_y+1][2*maze_x+1] = "⚑"
        #         elif self.show and self.path is not None and (maze_x, maze_y) in self.path:
        #             grid[2*maze_y+1][2*maze_x+1] = "▽"
        #         elif (maze_x, maze_y) in self.maze.fortytwo:
        #             grid[2*maze_y+1][2*maze_x+1] = "✹" 
        #         else:   
        #             grid[2*maze_y+1][2*maze_x+1] = " "
        #         grid[2*maze_y+1][2*self.maze.width] = "|"
        #         grid[2*self.maze.height][2*maze_x] = "+"
        #         grid[2*self.maze.height][2*maze_x+1] = "─"
        #         grid[2*self.maze.height][2*self.maze.width] = "+"
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
                if (maze_x, maze_y) in self.maze.fortytwo:
                    print(" ✹ ", end="")
                elif (maze_x, maze_y) == self.maze.entry:
                    print(" ▶ ", end="")
                elif (maze_x, maze_y) == self.maze.exit:
                    print(" ⚑ ", end="")
                else:
                    print("   ", end="")
            print("|")
        for maze_x in range(self.maze.width):
            cellval = self.maze.basegrid.cells[maze_y][maze_x]
            direction = Compass(cellval) 
            print("+", end="")
            print("───", end="")
        print("+")
        # for maze_y in range(0, self.maze.height):
        #     grid[2*maze_y+1][0] = "|"
        # for row in grid:
        #     print(" ".join(row))


if __name__ == "__main__":
    gen = MazeGenerator(
        width=10, height=10,
        entry=(0,0), exit=(9,9),
        perfect=True, seed=42
    )
    gen.generate()
    display = Display(gen)
    seed = 1
    while True:
        display.render()
        print ("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        choice = input("Choice? (1-4): ")
        if choice == "1":
            seed += 1
            gen.seed = seed
            random.seed(seed)
            gen.generate()
        elif choice == "2":
            if display.show is False:
                display.show = True
            else:
                display.show = False
        elif choice == "3":
            display.color = "pink"
        elif choice == "4":
            sys.exit(0)
