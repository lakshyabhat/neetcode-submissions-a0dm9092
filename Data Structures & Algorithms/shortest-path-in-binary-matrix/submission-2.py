class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        # 1. Edge Case: Start or End is blocked
        if grid[0][0] == 1 or grid[ROWS-1][ROWS-1] == 1:
            return -1
        
        queue = deque([(0, 0)])
        visit = set([(0, 0)])
        # Path length starts at 1 (the starting cell)
        length = 1 

        while queue:
            # Process everything at the current distance level
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                # If we reached the bottom-right corner
                if r == ROWS - 1 and c == ROWS - 1:
                    return length
                
                # All 8 directions
                directions = [
                    (0, 1), (0, -1), (1, 0), (-1, 0),
                    (1, 1), (-1, -1), (1, -1), (-1, 1)
                ]
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check boundaries and if cell is empty/unvisited
                    if (0 <= nr < ROWS and 0 <= nc < ROWS and 
                        grid[nr][nc] == 0 and (nr, nc) not in visit):
                        
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            
            # Finished processing one full step/level away
            length += 1
            
        return -1