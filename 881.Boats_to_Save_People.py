class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i=0
        j=len(people)-1
        c=0
        while i<=j:
            if people[j]==limit or people[i] + people[j] > limit :
                j-=1
                c+=1
            else:
                i+=1
                j-=1
                c+=1
        return c

        
