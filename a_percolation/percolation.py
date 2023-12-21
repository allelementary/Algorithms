class Percolation:

    def __init__(self, n: int):
        """creates n-by-n grid, with all sites initially blocked"""
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n
        self.open_sites = 0

    def open(self, row: int, col: int) -> None:
        """opens the site (row, col) if it is not open already"""
        if self.grid[row][col] == 0:
            self.grid[row][col] = 1
            self.open_sites += 1

    def is_open(self, row: int, col: int) -> bool:
        """is the site (row, col) open?"""
        return self.grid[row][col] == 1

    def is_full(self, row: int, col: int):
        """is the site (row, col) full?"""
        return self.grid[row][col] == 2

    def number_of_open_sites(self) -> int:
        """returns the number of open sites"""
        return self.open_sites

    def percolates(self) -> bool:
        """does the system percolate?"""
        grid_copy = [row[:] for row in self.grid]

        # Check for a_percolation from the top to the bottom of the grid
        for j in range(len(self.grid[0])):
            if grid_copy[0][j] == 1:
                self.dfs(grid_copy, 0, j)

        # If any site in the bottom row is marked as visited, the system percolates
        return any(row == 2 for row in grid_copy[-1])

    def dfs(self, grid: list, row: int, col: int):
        """Depth-first search to explore connected occupied sites"""
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] in [0, 2]:
            return

        grid[row][col] = 2  # Mark the site as visited
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)
