class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        i=0
        j=0
        c=0
        lt=len(trainers)
        lp=len(players)
        while i<lt and j<lp:
            if trainers[i]>=players[j]:
                j+=1
                i+=1
            else:
                i+=1
        return j
            
