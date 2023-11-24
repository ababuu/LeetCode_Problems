class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=len(fruits)
        if l==1 or l==2:
            return l
        i=0
        j=1
        c=1
        basket={fruits[0]:1}
        while j<l:
            if fruits[j] in basket:
                basket[fruits[j]]+=1
                j+=1
            elif len(basket)<2:
                basket[fruits[j]]=1
                j+=1
            else:
                c=max(c,j-i)
                while len(basket)==2:
                    basket[fruits[i]]-=1
                    if basket[fruits[i]]==0:
                        del basket[fruits[i]]
                    i+=1
        return max(c,j-i)
        
