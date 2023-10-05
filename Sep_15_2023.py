class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(points)
        edges = []  # List to store edges (distance, u, v)

        # Calculate distances between all pairs of points
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                edges.append((distance, i, j))

        # Sort edges by distance in ascending order
        edges.sort()

        parent = list(range(n))
        min_cost = 0

        for distance, u, v in edges:
            if find(parent, u) != find(parent, v):
                union(parent, u, v)
                min_cost += distance

        return min_cost