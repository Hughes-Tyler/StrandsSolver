word = "rabbit"
string_list = list(word)

print(string_list)

grid = [
    ['A', 'B', 'C', 't', 'x', 'F'],
    ['G', 'H', 'I', 'J', 'i', 'L'],
    ['M', 'N', 'O', 'b', 'Q', 'R'],
    ['r', 'w', 'b', 'p', 'x', 'x'],
    ['Y', 'a', 'A', 'x', 'C', 'D'],
    ['E', 'F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U', 'r']
]

def find_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, word, index, path):
        if index == len(word):
            return path
        if not is_valid(x, y) or grid[x][y] != word[index]:
            return None
        
        # Mark the current cell as visited
        temp = grid[x][y]
        grid[x][y] = "#"
        
        # Explore all 8 possible directions
        directions = [
            (0, 1),  # right
            (1, 0),  # down
            (0, -1), # left
            (-1, 0), # up
            (1, 1),  # down-right
            (1, -1), # down-left
            (-1, 1), # up-right
            (-1, -1) # up-left
        ]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            result = dfs(nx, ny, word, index + 1, path + [(nx, ny)])
            if result:
                return result
        
        # Unmark the current cell
        grid[x][y] = temp
        return None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                path = dfs(i, j, word, 0, [(i, j)])
                if path:
                    return path
    return []

positions = find_word_in_grid(grid, string_list)
if positions:
    print(f"Word '{word}' found at positions: {positions}")
else:
    print(f"Word '{word}' not found in the grid")
