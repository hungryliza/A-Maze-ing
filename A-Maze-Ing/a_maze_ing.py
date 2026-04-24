import random
import sys
from parser import parser
from mazegen import MazeGenerator
from visual_display import Display
from bfs import solve_maze

if __name__ == "__main__":
    maze_dict = parser()
    gen = MazeGenerator(maze_dict["width"], maze_dict["height"], maze_dict["entry"], maze_dict["exit"])
    maze = gen.generate()
    path = solve_maze(gen, maze)
    display = Display(gen, path)
    seed = 1
    while True:
        display.render()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")
        choice = input("Choice? (1-4): ")
        if choice == "1":
            seed += 1
            gen.seed = seed
            random.seed(seed)
            maze = gen.generate()
            path = solve_maze(gen, maze)
            display.maze = gen
            display.path = path
        elif choice == "2":
            if display.show is False:
                display.show = True
            else:
                display.show = False
        elif choice == "3":
            display.color = "blue"
        elif choice == "4":
            sys.exit(0)
