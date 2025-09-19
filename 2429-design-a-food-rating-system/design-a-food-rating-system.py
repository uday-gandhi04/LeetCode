class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foodDict={}
        self.cuisinesDict=defaultdict(list)

        for food,rating,cuisin in zip(foods,ratings,cuisines):
            self.foodDict[food]=[rating,cuisin]
            heapq.heappush(self.cuisinesDict[cuisin],(-rating,food))
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.foodDict[food][0]=newRating
        cuisin=self.foodDict[food][1]
        heapq.heappush(self.cuisinesDict[cuisin],(-newRating,food))

        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        
        out=self.cuisinesDict[cuisine][0]

        while self.foodDict[out[1]][0]!=-out[0]:
            heapq.heappop(self.cuisinesDict[cuisine])
            out=self.cuisinesDict[cuisine][0]
        
        return out[1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)