class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        target_state = (1 << n) - 1  # Target state is when all nodes are visited.
        queue = collections.deque()
        visited = set()

        # Initialize the queue with all nodes as starting points.
        for i in range(n):
            queue.append((i, 1 << i, 0))  # (node, state, distance)

        while queue:
            node, state, distance = queue.popleft()

            if state == target_state:
                return distance

            for neighbor in graph[node]:
                next_state = state | (1 << neighbor)

                # If we haven't visited this state before, add it to the queue.
                if (neighbor, next_state) not in visited:
                    visited.add((neighbor, next_state))
                    queue.append((neighbor, next_state, distance + 1))

        return -1