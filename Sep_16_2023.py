import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        left, right = 0, 10**6
        
        def isPossible(maxEffort):
            # Helper function to check if it's possible to reach the bottom-right cell
            # with a given maxEffort using BFS or Dijkstra's algorithm.
            visited = [[False] * cols for _ in range(rows)]
            queue = [(0, 0)]  # (row, col)
            
            while queue:
                row, col = queue.pop()
                visited[row][col] = True
                
                # Check adjacent cells
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                        diff = abs(heights[new_row][new_col] - heights[row][col])
                        if diff <= maxEffort:
                            queue.append((new_row, new_col))
            
            return visited[rows - 1][cols - 1]
        
        # Binary search to find the minimum maxEffort
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

# Example usage:
heights = [[1,2,2],[3,8,2],[5,3,5]]
solution = Solution()
print(solution.minimumEffortPath(heights))  # Output: 2