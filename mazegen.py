import random

class MazeGenerator:
    def __init__(self, width, height, entry, exit, perfect, seed, grid):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.grid = grid



if __name__ == "__main__":
    gen = MazeGenerator(
        width=20, height=15,
        entry=(0,0), exit=(19,14),
        perfect=True, seed=42
    )
    gen.generate()
    print(gen.grid)