class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # Create a list of tuples where each tuple contains the index of the row and the number of soldiers in that row
        rows_strength = [(i, sum(row)) for i, row in enumerate(mat)]

        # Sort the list of tuples based on the number of soldiers and then by row index
        rows_strength.sort(key=lambda x: (x[1], x[0]))

        # Extract the indices of the k weakest rows
        weakest_rows = [row[0] for row in rows_strength[:k]]

        return weakest_rows