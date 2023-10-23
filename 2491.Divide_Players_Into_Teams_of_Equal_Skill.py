class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        i=0
        j=len(skill)-1
        t=skill[i]+skill[j]
        c=0
        while i<j:
            s=skill[i]+skill[j]
            if s==t:
                c+=skill[i]*skill[j]
                i+=1
                j-=1
            else:
                return -1
        return c

        
