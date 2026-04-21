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

    def generate(self):
        self.pattern()

    def pattern(self):
        fortytwo = [(0,0),(0,1),(0,2),(1,2),(2,2),(2,3),(2,4),(4,0),
                    (5,0),(6,0),(6,1),(4,2),(5,2),(6,2),(4,3),(4,4),(5,4),(6,4)]
        placed = []
        placex = int((self.width - 7) / 2)
        placey = int((self.height - 6) / 2)
        for (i,j) in fortytwo:
            placed.append((i + placex, j + placey))
        return (placed)



if __name__ == "__main__":
    gen = MazeGenerator(
        width=20, height=15,
        entry=(0,0), exit=(19,14),
        perfect=True, seed=42
    )
    gen.pattern(7, 5)
    gen.generate()
    print(gen.basegrid.cells)
