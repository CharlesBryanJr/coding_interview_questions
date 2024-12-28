class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = [False] * len(candies)
        greatest_number_of_candies = max(candies)
        for i in range(len(candies)):
            candy_count = candies[i]
            if candies[i] + extraCandies >= greatest_number_of_candies:
                result[i] = True
        return result