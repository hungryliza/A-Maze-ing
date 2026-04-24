from collections import deque


def solve_maze(self, grid):
    start_y, start_x = self.entry
    exit_y, exit_x = self.exit
    width = self.width
    height = self.height

    q = deque([(start_x, start_y)])
    visited = {(start_x, start_y)}
    way = {(start_x, start_y): None}

    directions = [
        (0, -1, 1, 4),
        (1, 0, 2, 8),
        (0, 1, 4, 1),
        (-1, 0, 8, 2)
    ]
    found = False
    while q:
        curr_x, curr_y = q.popleft()
        if (curr_x, curr_y) == (exit_x, exit_y):
            found = True
            break
        for dx, dy, wall, wall_next in directions:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == 16:
                    continue
                if not (grid[curr_y][curr_x]) & wall and \
                     not (grid[ny][nx] & wall_next) and \
                        (nx, ny) not in visited:
                    visited.add((nx, ny))
                    way[(nx, ny)] = (curr_x, curr_y)
                    q.append((nx, ny))
    path = []
    if found:
        curr = (exit_x, exit_y)
        while curr is not None:
            path.append(curr)
            curr = way.get(curr)
        return path[::-1]
    return []
