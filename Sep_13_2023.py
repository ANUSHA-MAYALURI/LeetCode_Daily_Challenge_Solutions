class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candies = [1] * n  # Initialize candies for all children to 1
        
        # Forward pass to ensure higher-rated children get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Backward pass to fix any inconsistencies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Calculate the total number of candies
        total_candies = sum(candies)
        
        return total_candies