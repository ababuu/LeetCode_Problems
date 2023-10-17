class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        l=len(piles)
        m=0
        i=l/3
        while i<l-1:
            m+=piles[i]
            i+=2
        return m
