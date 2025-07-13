class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        n=len(trainers)
        i=0
        out=0
        for p in players:
            if i==n:
                break
            if p<=trainers[i]:
                out+=1
                i+=1
        return out

        