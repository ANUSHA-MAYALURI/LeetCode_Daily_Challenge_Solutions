class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Create a graph to store the adjacency list of airports
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        # Sort the destinations in lexical order for each airport
        for key in graph:
            graph[key].sort()

        # Initialize the result itinerary with the starting airport, "JFK"
        result = ["JFK"]

        # Define a recursive DFS function to find the itinerary
        def dfs(node):
            result
            if len(result) == len(tickets) + 1:
                return True  # We have found a valid itinerary

            if node not in graph:
                return False  # Dead-end, backtrack

            destinations = graph[node]
            for i, dest in enumerate(destinations):
                graph[node].pop(i)  # Mark the ticket as used
                result.append(dest)
                if dfs(dest):
                    return True
                result.pop()  # Backtrack

                # Restore the removed ticket for trying the next destination
                graph[node].insert(i, dest)

            return False

        # Start DFS from "JFK"
        dfs("JFK")
        return result