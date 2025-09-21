class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.n=n
        self.unrentedMovies=defaultdict(list)
        self.heap=[]
        self.movieInfo={}

        for shop,movie,price in entries:
            heapq.heappush(self.unrentedMovies[movie],(price,shop,movie))
            self.movieInfo[(movie,shop)]=[price,0]


    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        out=[]
        
        temp=[]

        while self.unrentedMovies[movie] and len(out)<5:
            m=heapq.heappop(self.unrentedMovies[movie])
            shop=m[1]

            if not self.movieInfo[(movie,shop)][1] and m not in temp:
                out.append(m[1])
                temp.append(m)
        
        for entry in temp:
            heapq.heappush(self.unrentedMovies[movie],entry)
        
        return out
        

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price=self.movieInfo[(movie,shop)][0]
        self.movieInfo[(movie,shop)][1]=1
        heapq.heappush(self.heap,(price,shop,movie))
        

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        self.movieInfo[(movie,shop)][1]=0
        price = self.movieInfo[(movie, shop)][0]
        heapq.heappush(self.unrentedMovies[movie], (price, shop, movie))
        

    def report(self):
        """
        :rtype: List[List[int]]
        """

        
        temp=[]
        out=[]

        while self.heap and len(out)<5:
            m=heapq.heappop(self.heap)
            price,shop,movie=m[0],m[1],m[2]

            if self.movieInfo[(movie,shop)][1] and (price,shop,movie) not in temp:
                out.append([shop,movie])
                temp.append((price,shop,movie))
        
        for entry in temp:
            heapq.heappush(self.heap,entry)
        

        return out





# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()