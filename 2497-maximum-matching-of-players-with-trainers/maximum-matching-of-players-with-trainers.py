class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        n=len(trainers)
        i=0
        out=0
        for p in players:
            while i<n:
                if trainers[i]>=p:
                    out+=1
                    i+=1
                    break
                i+=1
        return out

        