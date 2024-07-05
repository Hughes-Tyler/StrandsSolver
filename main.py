from termcolor import colored

words_to_search = [
    "rabbit", "apple", "cat", "dog", "fish", "goat", "hat",
    "ice", "juice", "kite", "lion", "monkey", "nose", "orange",
    "pencil", "queen", "rabbit", "snake", "tiger", "umbrella",
    "vase", "whale", "x-ray", "yogurt", "zebra"
]

grid = [
    ['t', 'x', 'x', 'x', 'x', 'x'],
    ['i', 'b', 'x', 'x', 'x', 'x'],
    ['a', 'b', 'x', 'x', 'x', 'e'],
    ['r', 'x', 'x', 'x', 'l', 'x'],
    ['x', 'a', 'p', 'p', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x'],
    ['i', 'e', 'x', 'x', 'x', 'x'],
    ['c', 'x', 'x', 'x', 'x', 'x']
]

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def search_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    
    def dfs(x, y, word, index, path):
        if index == len(word):
            return path
        if not is_valid(x, y, rows, cols) or grid[x][y] != word[index]:
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

found_words = {}

for word in words_to_search:
    grid_copy = [row[:] for row in grid]  # Create a copy of the grid for each word
    positions = search_word(grid_copy, word)
    if positions:
        found_words[word] = positions

if found_words:
    for word, positions in found_words.items():
        print(f"Word '{word}' found at positions: {positions}")
else:
    print("No words found in the grid")