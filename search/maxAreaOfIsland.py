
def maxAreaOfIsland(grid) -> int:
	max_area = 0
	row, col = len(grid), len(grid[0])
	for r in range(row):
		for c in range(col):
			if grid[r][c] == 1:
				area = dfs(grid, r, c)
				max_area = area if area > max_area else max_area
	return max_area

def dfs(grid, i, j):
	stack = [(i, j)]
	count = 0
	row, col = len(grid), len(grid[0])
	while (stack):
		(r, c) = stack.pop()
		if grid[r][c] == 1:
			if r > 0:
				stack.append((r - 1, c))
			if c > 0:
				stack.append((r, c - 1))
			if r < row - 1:
				stack.append((r + 1, c))
			if c < col - 1:
				stack.append((r, c + 1))
			count += 1
			grid[r][c] = 0
	return count

test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(test))